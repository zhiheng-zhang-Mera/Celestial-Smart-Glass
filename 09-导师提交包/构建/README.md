# 正式文档构建

本目录保存从本提交包 Markdown 生成 Word 的排版脚本；PDF 由 Word 文档渲染得到。脚本不是智能眼镜产品实现，不采集或处理参与者数据。

- [build_submission.py](build_submission.py)：标题层级、目录、表格、来源引用、图片、页码与 Word 文件生成。
- [generate_figures.py](generate_figures.py)：生成研究架构与回放实验示意图，不表示真实设备截图或完成的系统。
- [目录页码.json](目录页码.json)：本版主计划和实施附件中主要章节的已核对页码；内容或排版变化后必须重新检查。

依赖：Python、python-docx、matplotlib、Pillow。正式生成使用任务环境的 `CODEX_PRIMARY_RUNTIME_PYTHON`。本次中文排版使用 Noto Sans CJK SC；可通过 `CSG_FONT_DIR` 指定包含 Regular/Bold OTF 的目录。未安装该字体时，需先准备合适中文字体，避免生成缺字文档。字体来源：[Noto CJK 官方仓库](https://github.com/notofonts/noto-cjk)。字体不打包进入本项目。

脚本只覆盖本提交包内固定名称的正式输出，保留 Markdown 内容来源。最终交付前须渲染并逐页检查 Word/PDF；生成成功不等于视觉核验通过。目录页码来自最终 PDF 的检查后映射，不能凭空填写。

## 从仓库根目录生成

在已安装上述依赖和中文字体的 Python 环境中运行：

```bash
python3 09-导师提交包/构建/generate_figures.py
python3 09-导师提交包/构建/build_submission.py --toc-pages 09-导师提交包/构建/目录页码.json
```

`generate_figures.py` 可通过 `CSG_FONT_DIR` 选择字体目录。构建脚本的 `--only main`、`--only appendix`、`--only brief` 分别生成一份 Word；不传 `--only` 则生成三份。引用从 [07 文献与证据的参考文献](../../07-文献与证据/参考文献.md)按实际引用顺序生成，正文引用链接与文末文献同时更新。

Word 生成后，用支持中文字体的 Word 或 LibreOffice 导出 PDF。本次使用文档工具的 `render_docx.py` 完成导出及逐页 PNG 渲染；该渲染工具属于工作环境，不是本仓库产品依赖。重新排版时先导出一次，核对章节实际页码，更新 `目录页码.json`，再生成 Word 和最终 PDF。不同字体、Office 版本及换行行为可能改变页数，不能直接沿用旧页码。

核验重点：所有页面无缺字、表格截断或内容重叠；图片与标题对应；目录页码准确；正文引用有定义；三份文档的方法、样本量、平台状态和版本一致。最终核验结果见[文档版本与核验](../文档版本与核验.md)。

[返回提交包](../README.md)
