"""Generate exact proposal diagrams. These are proposed designs, not measurements."""
from pathlib import Path
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle

PACKAGE = Path(__file__).resolve().parents[1]
FONT_DIR = Path(os.environ.get('CSG_FONT_DIR', 'fonts'))
for p in FONT_DIR.glob('*.otf'):
    font_manager.fontManager.addfont(str(p))
plt.rcParams.update({'font.family': 'Noto Sans CJK SC', 'font.size': 11,
                     'axes.unicode_minus': False, 'savefig.facecolor': 'white'})
OUT = PACKAGE / '图示'
OUT.mkdir(exist_ok=True)
INK = '#23313b'
ACCENT = '#35616a'
GRAY = '#5c6369'

def box(ax, x, y, w, h, title, detail='', fill='white'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.08',
                              linewidth=1.2,edgecolor=INK,facecolor=fill))
    if detail:
        ax.text(x+w/2,y+h*.65,title,ha='center',va='center',fontsize=11.5,color=INK,weight='bold')
        ax.text(x+w/2,y+h*.27,detail,ha='center',va='center',fontsize=9.4,color=GRAY)
    else:
        ax.text(x+w/2,y+h/2,title,ha='center',va='center',fontsize=11,color=INK)

def arrow(ax, a, b, dashed=False):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=13,
                               color=ACCENT,linewidth=1.4,linestyle='--' if dashed else '-'))

fig,ax=plt.subplots(figsize=(10,7.3))
ax.set(xlim=(0,10),ylim=(0,7.3)); ax.axis('off')
ax.text(.25,7.05,'拟议系统架构',fontsize=15,weight='bold',color=INK)
ax.text(.25,6.72,'核心字幕路径独立运行；模型只提出候选建议',fontsize=10,color=GRAY)
box(ax,.3,5.4,3.4,.95,'语音输入或固定回放','源时间  ·  授权  ·  质量')
box(ax,5.9,5.4,3.8,.95,'可选本人信号','Watch  ·  获准 sEMG  ·  本人自述',fill='#f3f6f6')
box(ax,.3,3.9,3.4,.95,'稳定字幕与会话角色','同一转写轨迹  ·  A B C 或未知')
box(ax,5.9,3.9,3.8,.95,'个人基线与活动对照','动作识别与意义解释分开',fill='#f3f6f6')
box(ax,.3,2.35,3.4,1.0,'补充线索候选','规则或固定模型  ·  证据与时效')
box(ax,5.9,2.35,3.8,1.0,'独立日常支持政策','另行选择  ·  单独评价',fill='#f3f6f6')
box(ax,.3,.65,3.4,1.05,'确定性呈现控制器','有效性  ·  容量  ·  可选门控')
box(ax,5.9,.65,3.8,1.05,'眼镜显示与手动控制','字幕优先  ·  忽略  ·  暂停  ·  退出')
arrow(ax,(2,5.4),(2,4.85)); arrow(ax,(2,3.9),(2,3.35)); arrow(ax,(2,2.35),(2,1.7))
arrow(ax,(7.8,5.4),(7.8,4.85),True); arrow(ax,(7.8,3.9),(7.8,3.35),True)
arrow(ax,(7.8,2.35),(7.8,1.7),True); arrow(ax,(3.7,1.17),(5.9,1.17))
ax.plot([3.7,4.65,4.65,5.7],[4.37,4.37,1.5,1.5],color=ACCENT,linewidth=1.4)
arrow(ax,(5.7,1.5),(5.9,1.5))
ax.text(4.78,3.1,'字幕直达\n不等待模型',fontsize=8.6,ha='left',color=GRAY,
        bbox={'facecolor':'white','edgecolor':'none','pad':2})
ax.text(.3,.15,'实线为首年核心路径；虚线为可选分支。两类解释不相互替代。',fontsize=9.5,color=GRAY)
fig.savefig(OUT/'csg_architecture.png',dpi=200,bbox_inches='tight'); plt.close(fig)

fig,ax=plt.subplots(figsize=(10,6.8))
ax.set(xlim=(0,10),ylim=(0,6.8)); ax.axis('off')
ax.text(.25,6.53,'拟议回放研究情境',fontsize=15,weight='bold',color=INK)
ax.text(.25,6.18,'受控比较检验理解与信息整合；真实互动另行评价',fontsize=10,color=GRAY)
ax.add_patch(Rectangle((.45,3.8),4.7,1.95,edgecolor=INK,facecolor='#f5f6f7',linewidth=1.4))
for x,tag in [(1.35,'A'),(2.8,'B'),(4.25,'C')]:
    ax.add_patch(Circle((x,4.95),.23,edgecolor=INK,facecolor='white',linewidth=1.2))
    ax.plot([x-.35,x-.25,x+.25,x+.35],[4.3,4.62,4.62,4.3],color=INK,linewidth=1.2)
    ax.text(x,4.08,tag,ha='center',fontsize=10,color=INK)
ax.text(2.8,3.48,'同框人物视频与原始音频',ha='center',fontsize=11,color=INK)
box(ax,5.8,3.8,3.7,1.95,'眼镜内研究界面','会话内来源标签与字幕\n共享基础层 + 单个补充槽')
ax.text(7.65,3.48,'屏幕相对组织  非世界锁定',ha='center',fontsize=10,color=GRAY)
box(ax,.45,1.8,4.7,1.05,'按日常方式观看','保留助听与沟通支持  ·  条件间一致')
box(ax,5.8,1.8,3.7,1.05,'每段后在伴随界面作答','相同题目流程  ·  可访问输入方式')
arrow(ax,(2.8,3.31),(2.8,2.85)); arrow(ax,(7.65,3.31),(7.65,2.85))
arrow(ax,(5.15,2.33),(5.8,2.33))
ax.text(.45,1.2,'每人 18 段对话  ·  三条件各 6 段  ·  主要题共 36 道',fontsize=11,color=INK)
ax.text(.45,.72,'三条件使用不同匹配材料；条件顺序与材料分配联合平衡。',fontsize=10,color=GRAY)
ax.text(.45,.28,'屏幕尺寸、座距、字号与音量在试点后记录并冻结。此图不是实际研究现场。',fontsize=9.5,color=GRAY)
fig.savefig(OUT/'csg_study_setup.png',dpi=200,bbox_inches='tight'); plt.close(fig)
print('Generated',len(list(OUT.glob('*.png'))),'proposal diagrams')
