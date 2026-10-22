# Uncertainty-Aware Conversational Assistance on Smart Glasses

## Adaptive speaker-aware captions, user-controlled cues, and an optional self-awareness extension

**PhD research proposal draft — 22 October 2026**

**Applicant: Zhiheng Zhang**

Proposed research discussion with Dr Xueliang Li, School of Design, Southern University of Science and Technology. Participant studies and device validation remain proposed; synthetic design-sensitivity calculations have been run. Supervision, partnerships, access, and approvals remain to be confirmed. This concise application draft accompanies the [full research plan](../09-导师提交包/完整研究计划.md) and [implementation appendix](../09-导师提交包/研究实施附件.md).

## 1. Research motivation and positioning

I propose to investigate how commercial smart glasses can support deaf and hard-of-hearing (DHH) adults in small-group spoken conversations without surrendering interpretive control to AI. The first-year system will combine stable, speaker-aware captions with a small, optional vocabulary of supplementary cues. Its central mechanism will decide when information should be displayed, deferred, or withheld. Meta Ray-Ban Display is the initial hardware candidate; Jev is a replaceable structured decision component, not the research contribution itself.

Group interaction requires identifying speakers, following turn relationships, and interpreting delivery. SpeechBubbles established spatial-captioning precedents with DHH participants [HCI-01]. VocalEyes investigated speaker-aware AR captions with participants reporting typical hearing; it remains a preprint [HCI-06]. Mixed-hearing group co-design further identifies shared norms and relationships as access concerns [HCI-14].

Research on ASR confidence and expressive captions, including Caption Royale, establishes potential value alongside tensions between information, legibility, familiarity, and distraction [HCI-02, HCI-03, HCI-09]. CuCap and Fuzzy Feelings highlight differences in interpreting feedback [HCI-04, HCI-05]. The proposed contribution concerns receiving and controlling uncertain assistance on a constrained display, not recognizing hidden emotions.

The broader concept combines shared temporary conversational context, incremental text commitment, and source isolation. Translation and multimodal interpretation may later share this infrastructure, but inferred cues must never rewrite the transcript. Cross-language interpretation and unrestricted social inference are outside the first-year core.

## 2. Aim and research questions

The aim is to preserve access to speech while helping users manage the uncertainty and visual cost of additional information.

- **RQ1 — Needs:** Which cues do DHH adults find useful, distracting, or socially unwelcome, and what boundaries should govern them?
- **RQ2 — Presentation:** How does uncertainty- and display-load-aware presentation affect interpretation accuracy, effort, and inappropriate reliance?
- **RQ3 — Recovery:** How do users respond to wrong, missing, ambiguous, or stale cues, and which controls preserve agency?
- **RQ4 — Exploratory self-awareness:** Can optional feedback about the wearer's physiological changes and self-selected hand habits support reflection without unnecessary interruption or pathologizing behavior?

Selective presentation may reduce distraction while retaining useful information. Captions alone may nevertheless perform better, and preferences may differ substantially. These are meaningful possible findings, not exceptions to be explained away.

## 3. Scope and proposed system

The core population is adults who identify as DHH and choose written captions; they will not represent all Deaf people. Initial tasks involve two or three stationary speakers indoors, using one language selected with recruitment partners. Access arrangements follow participants' preferences.

The common interface will provide stable captions, anonymous session-level speaker labels, and conservative screen-relative placement. Directional cues require validated attribution; unresolved identity produces an unknown-speaker state. Candidate additions include overlap, emphasis, relative speaking-rate changes, and narrowly defined communicative acts selected through co-design. Observed acoustic features and inferred acts will be visibly distinguished. Deception, attraction, personality, and hidden emotion will not be classification targets.

A phone or laboratory computer will run recognition, diarization, and feature extraction. Temporary context will hold utterances, timestamps, quality indicators, and display occupancy. Each cue retains its evidence, version, age, expiry, and suppression reason. Pause, dismissal, category selection, and caption-only mode enact user-control principles [HCI-08]. Display occupancy is not a direct cognitive-load measure.

Jev refers to TypeSafe's decision model, not V-JEPA. It receives text and structured events, not raw audio/video; experimental images are not a dependency [JEV-01, JEV-03]. An independent controller enforces consent, validity, expiry, and settings. API confidence is not task-specific correctness probability; thresholds require held-out evaluation and external calibration [JEV-02]. Version-pinned Jev will be compared with rules and a feasible alternative classifier. Replacement preserves the HCI question.

Display access, audio routes, permissions, latency, and distribution restrictions require audit [META-01, META-02]. Eye tracking, synchronized microphone-array channels, and world-locked 3D anchors are not assumed. Supported laboratory hardware or explicitly labelled simulation remains a fallback, with deployment claims narrowed accordingly.

## 4. First-year methodology

### Participatory design and technical preparation

After ethics approval, six to eight DHH adults will join compensated, accessible interviews and co-design. Scenarios address misattribution, unwanted interpretations, ambiguity, and crowding. Partner perspectives will not override wearers' preferences. Research through Design will inform records of alternatives, rejection, and situated rationale [METHOD-02, METHOD-03]. This design knowledge will remain distinct from controlled policy effects and qualitative recovery accounts.

Materials will distinguish scripted intent, independent annotation, and participant interpretation. Hidden emotion is not ground truth; ambiguous items support abstention testing or qualitative inquiry. Speaker/conversation splits precede threshold tuning. Offline evaluation covers errors, coverage, selective risk, latency, and cue age. Human corrections provide reference text only: each clip's displayed ASR trace is frozen identically across conditions.

A four- to six-person pilot will refine accessibility, difficulty, fatigue management, and instrumentation—not select items according to which condition wins. Cue pools, models, thresholds, materials, exclusions, and analysis will then be frozen, with display limits and lifetimes in a versioned parameter sheet.

### Controlled evaluation

A within-participant study provisionally targets 24 randomized DHH adults. Completed synthetic design-sensitivity simulations for N=24/36/48 retain crossed variability and allocation structure. They assess repeated-sampling error of descriptive paired accuracy differences, not full GLMM power or final interval coverage. Recruitment and stopping rules will be fixed before main outcomes are visible; limited precision may require exploratory interpretation. [Calculation details](../05-实验与评估/样本量与精度规划.md) document assumptions and results.

Participants view 18 prerecorded 45–60-second clips: three matched sets of six clips, each with three two-speaker and three three-speaker conversations. Two questions follow each clip, totaling 36. Each condition receives one set; six condition orders and material assignments are jointly balanced, without repeated clips per participant.

All speakers appear together on one screen; glasses provide captions and view-relative labels. Normal audiovisual access and usual hearing aids remain available. Questions appear afterward on the same companion interface. They require cross-turn integration, not copying cue labels. This evaluates replay comprehension, not unrestricted live participation. Co-design selects the layout; all conditions share the frozen ASR trace, timing, typography, adaptation rules, and speaker mapping:

| Condition | Supplementary information |
| --- | --- |
| C0: Captions only | No supplementary cues |
| C1: Baseline-scheduled assistance | Valid candidates enter shared capacity and scheduling rules, without optional uncertainty/load filtering |
| C2: Gated assistance | The same candidates and baseline rules, plus the frozen selective policy |

C1/C2 share validity, identity, expiry, capacity, and queue rules: C1 does not guarantee every candidate is displayed. Cue generation is frozen. Participant-approved initial settings are common across conditions; later opt-outs persist unless the wearer chooses otherwise. Layout effects are not independently identified.

The **primary estimand is Δ20, the standardized accuracy difference C2−C0 on prespecified low-ambiguity questions**, reported in percentage points with a two-sided 95% confidence interval. The secondary accuracy family contains Δ21 (C2−C1) and Δ10 (C1−C0), each with a Bonferroni-adjusted 97.5% interval. Effort, discomfort, interruptions, exposure, and agency are descriptive outcomes. Separate recovery probes distinguish incorrect output, correct abstention, and reasonable disagreement; they do not enter primary accuracy scoring.

A proposed binomial mixed model addresses participants, items, clips, and condition heterogeneity; diagnostics, bootstrap intervals, missingness, and fallback rules appear in the [analysis draft](../05-实验与评估/统计分析预注册草案.md). Non-significance implies neither equivalence nor safety. C2−C1 estimates the net policy effect, including density changes; it cannot isolate calibration from fewer interruptions. Density-matched evaluation is deferred.

### Optional live extension

If technical and comfort criteria are met, six to eight participants may undertake brief live conversations with consenting partners. Logs and participant-selected episode replay examine attribution, repair, and acceptability. This supports feasibility and experience claims, not long-term participation or well-being effects.

## 5. Optional daily self-awareness module

RQ4 is a separate pilot with eight to twelve consenting adults over approximately two weeks, conditional on approval and signal access. Participants select one or two habits they wish to understand. Manual reflection, HR plus activity context, and those inputs plus selected motor patterns will inform feasibility, not comparative efficacy.

MindSeed connects fidgeting data with reflection; Grippy illustrates awareness and unwanted burden [LI-04, LI-05]. Neither validates unconscious-action classification. HR/HRV can diverge from experienced stress [HRV-01, HRV-02]; decoding instructed sEMG gestures does not establish arbitrary spontaneous-behavior interpretation [EMG-01]. Whether an event was unnoticed requires the wearer's account.

Consumer Neural Band command events must not be presented as raw muscle recordings. Research access through Aria is a distinct pathway [META-03, META-04]. Apple Watch measurement, HealthKit storage, and application delivery timing require separate checks [APPLE-01, APPLE-02]. Without adequate access, the module will use manual reflection or approved research equipment, or be deferred. Evaluation will emphasize false prompts per hour, contextual interpretation, autonomy, and burden. Harmless fidgeting will not be something the system automatically tries to suppress.

## 6. Ethics, feasibility, and doctoral development

Institutional approval will precede recruitment. Everyone whose speech or image is processed must consent; uninvolved bystanders will not be analyzed. Runtime buffers will be bounded and minimized, with research recordings governed separately. The broader concept's 90-second buffer is not a mandatory retention target. Semantic summaries can remain sensitive even after footage is deleted.

Third-party processing requires institutional approval and applicable agreements. A provider's statement that inputs are not used for training does not establish zero retention [JEV-04]. Public artifacts will contain designs, synthetic examples, and permitted code—not participant recordings, physiological traces, identity embeddings, or credentials. Participants may pause or withdraw; discomfort or loss of usable access support triggers a break. No diagnostic or therapeutic claim is intended.

Months 1–2 will establish device feasibility, community relationships, and ethics; months 3–4 will support co-design; months 5–6 will deliver the replay prototype and offline analysis; month 7 will pilot and freeze the protocol; months 8–10 will conduct the main study; months 11–12 will analyze and write. Optional extensions can be postponed. Minimum success is a reproducible policy evaluation and grounded design reasoning, not product release or publication acceptance.

The project fits Dr Li's situated interaction and human–wearable research [LI-00]. His CSCW 2026 work informs stakeholder perspectives; Reminiscope informs participant-shaped AI experiences; MindSeed and the earlier Grippy motivate reflection and negotiable support [LI-02, LI-03, LI-04, LI-05]. These methodological connections do not imply direct transfer to DHH conversation. Contributions will distinguish co-designed presentation principles, controlled evidence of policy effects, and qualitative knowledge about recovery and agency.

## Source references

Keys below resolve to explicit primary or official sources. The complete catalog, including the original proposal's 18 references and evidence limitations, is in [参考文献](../07-文献与证据/参考文献.md).

- [HCI-01] Peng et al. (2018). *SpeechBubbles*. https://doi.org/10.1145/3173574.3173867
- [HCI-02] Berke, Caulfield, and Huenerfauth (2017). *DHH Perspectives on Imperfect ASR*. https://doi.org/10.1145/3132525.3132541
- [HCI-03] de Lacerda Pataca et al. (2023). *Visualization of Speech Prosody and Emotion in Captions*. https://doi.org/10.1145/3544548.3581511
- [HCI-04] de Lacerda Pataca et al. (2025). *CuCap*. https://doi.org/10.1145/3663547.3746400
- [HCI-05] de Lacerda Pataca et al. (2026). *Fuzzy Feelings*. https://doi.org/10.1145/3772318.3793421
- [HCI-06] Wang et al. (2026). *VocalEyes*. Preprint. https://arxiv.org/abs/2609.32983
- [HCI-08] Amershi et al. (2019). *Guidelines for Human-AI Interaction*. https://doi.org/10.1145/3290605.3300233
- [HCI-09] de Lacerda Pataca et al. (2024). *Caption Royale*. https://doi.org/10.1145/3613904.3642258
- [HCI-14] McDonnell et al. (2023). *“Easier or Harder, Depending on Who the Hearing Person Is”*. https://doi.org/10.1145/3544548.3580809
- [METHOD-02] Zimmerman, Forlizzi, and Evenson (2007). *Research Through Design as a Method for Interaction Design Research in HCI*. https://doi.org/10.1145/1240624.1240704
- [METHOD-03] Gaver (2012). *What Should We Expect From Research Through Design?* https://doi.org/10.1145/2207676.2208538
- [LI-00] SUSTech. Faculty profile. https://designschool.sustech.edu.cn/about/team/faculty/483.html
- [LI-02] Li et al. (2026). *“It Seems Every Word They Say Has a Purpose”*. https://doi.org/10.1145/3788061
- [LI-03] Zhu et al. (2026). *Remembering with Reminiscope*. https://doi.org/10.1145/3772318.3791390
- [LI-04] Jin, Xue, and Li (2026). *MindSeed*. https://doi.org/10.1145/3800645.3813047
- [LI-05] Li et al. (2022). *Get a Grip on Stress with Grippy!*. https://doi.org/10.57698/v16i3.06
- [HRV-01] Velmovitsky et al. (2023). Apple Watch ECG and stress. https://doi.org/10.3389/fpubh.2023.1178491
- [HRV-02] Martinez et al. (2022). HRV and perceived stress in situ. https://doi.org/10.2196/33754
- [EMG-01] Kaifosh, Reardon, and CTRL-labs (2025). Neuromotor interface. https://doi.org/10.1038/s41586-025-09255-w
- [META-01] Device Access Toolkit. https://developers.meta.com/wearables/device-access-toolkit/
- [META-02] DAT iOS changelog. https://github.com/facebook/meta-wearables-dat-ios/blob/main/CHANGELOG.md
- [META-03] Consumer display/band description. https://www.meta.com/en-gb/blog/meta-ray-ban-display-ai-glasses-connect-2025/
- [META-04] Aria research SDK changelog. https://facebookresearch.github.io/projectaria_tools/gen2/ark/client-sdk/changelog
- [APPLE-01] Heart-rate measurements. https://support.apple.com/en-us/120277
- [APPLE-02] Heart-rate accuracy study. https://www.apple.com/health/pdf/Heart_Rate_Accuracy_Study_2026.pdf
- [JEV-01] Models. https://docs.typesafe.ai/models
- [JEV-02] Confidence. https://docs.typesafe.ai/confidence
- [JEV-03] Images. https://docs.typesafe.ai/images
- [JEV-04] Data handling. https://help.typesafe.ai/articles/5974925716-how-is-submitted-data-used-or-retained
