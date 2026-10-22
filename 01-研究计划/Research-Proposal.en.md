# Uncertainty-Aware Conversational Assistance on Smart Glasses

## Adaptive speaker-aware captions, user-controlled cues, and an optional self-awareness extension

**PhD research proposal draft — 22 October 2026**

**Applicant: Zhiheng Zhang**

Proposed research discussion with Dr Xueliang Li, School of Design, Southern University of Science and Technology. All studies and capabilities below are proposed, not completed. Supervision, recruitment partnerships, hardware access, and institutional approvals remain to be confirmed.

## 1. Research motivation and positioning

I propose to investigate how commercial smart glasses can support deaf and hard-of-hearing (DHH) adults in small-group spoken conversations without surrendering interpretive control to AI. The first-year system will combine stable, speaker-aware captions with a small, optional vocabulary of supplementary cues. Its central mechanism will decide when information should be displayed, deferred, or withheld. Meta Ray-Ban Display is the initial hardware candidate; Jev is a replaceable structured decision component, not the research contribution itself.

Captions provide access to words, but group interaction also requires identifying speakers, following turn relationships, and interpreting delivery. Spatial captioning is already established: SpeechBubbles examined these issues with DHH participants [HCI-01]. The recent VocalEyes preprint investigated speaker-aware AR captions, but evaluated participants reporting typical hearing [HCI-06]. Neither establishes that one layout transfers unchanged to a small consumer display.

Supplementary information also has costs. Research on ASR confidence and expressive captions identifies tension between information, legibility, familiarity, and distraction [HCI-02, HCI-03, HCI-04]. Fuzzy Feelings highlights differences in interpreting affect-related feedback [HCI-05]. The proposed contribution is therefore not another claim to recognize emotion, but evidence about receiving and controlling uncertain assistance in a constrained display.

The broader concept combines shared temporary conversational context, incremental text commitment, and source isolation. Translation and multimodal interpretation may later share this infrastructure, but inferred cues must never rewrite the transcript. Cross-language interpretation and unrestricted social inference are outside the first-year core.

## 2. Aim and research questions

The aim is to preserve access to speech while helping users manage the uncertainty and visual cost of additional information.

- **RQ1 — Needs:** Which cues do DHH adults find useful, distracting, or socially unwelcome, and what boundaries should govern them?
- **RQ2 — Presentation:** How does uncertainty- and display-load-aware presentation affect interpretation accuracy, effort, and inappropriate reliance?
- **RQ3 — Recovery:** How do users respond to wrong, missing, ambiguous, or stale cues, and which controls preserve agency?
- **RQ4 — Exploratory self-awareness:** Can optional feedback about the wearer's physiological changes and self-selected hand habits support reflection without unnecessary interruption or pathologizing behavior?

Selective presentation may reduce distraction while retaining useful information. Captions alone may nevertheless perform better, and preferences may differ substantially. These are meaningful possible findings, not exceptions to be explained away.

## 3. Scope and proposed system

The core population is adults who identify as DHH and choose written captions for spoken interaction. They will not represent all Deaf people. Initial tasks will involve two or three stationary speakers in private indoor settings, using one primary language selected with recruitment partners. Access arrangements will follow participants' preferences.

The common interface will provide stable captions, anonymous session-level speaker labels, and conservative screen-relative placement. Directional cues require validated attribution; unresolved identity produces an unknown-speaker state. Candidate additions include overlap, emphasis, relative speaking-rate changes, and narrowly defined communicative acts selected through co-design. Observed acoustic features and inferred acts will be visibly distinguished. Deception, attraction, personality, and hidden emotion will not be classification targets.

A phone or laboratory computer will run speech recognition, diarization, and feature extraction. Temporary context will hold recent utterances, timestamps, quality indicators, and display occupancy. Each candidate cue will retain its evidence, version, creation time, expiry, and suppression reason. Pause, dismissal, category selection, and caption-only mode will be available. Display occupancy is an engineering measure, not a direct measurement of cognitive load.

Jev refers to TypeSafe's decision model, not V-JEPA. It will receive text and structured events, not raw audio or video [JEV-01]. Experimental image support is not a core dependency [JEV-03]. An independent controller will enforce consent, validity, expiry, and user settings. The API's confidence statistic is not automatically the probability of correctness in this task; thresholds require held-out evaluation and external calibration where labels permit [JEV-02]. Version-pinned Jev will be compared with rules and a feasible alternative classifier. Replacement will not invalidate the HCI question.

Device documentation supports investigation, not a claim of implementation. Actual display access, audio routes, permissions, latency, and distribution restrictions will be audited [META-01, META-02]. Eye tracking, synchronized microphone-array channels, and world-locked 3D anchors will not be assumed. If necessary, supported laboratory hardware or explicitly labelled simulation will be used, with deployment claims correspondingly narrowed.

## 4. First-year methodology

### Participatory design and technical preparation

After ethics approval, approximately six to eight DHH adults will join compensated, accessible interviews and co-design. Scenario cards will address misattributed captions, unwanted interpretations, ambiguity, and crowded displays. Optional partner interviews will examine shared expectations without overriding wearers' access preferences. Two or three interface alternatives and their rejection or revision will form a design-rationale record. Participants may reject entire cue categories.

An annotated conversational corpus will include clear events, overlapping speech, errors, and missing context. Scripted intent, independent annotation, and participant interpretation will remain separate. Hidden emotion will not serve as ground truth; ambiguous items will support abstention testing or qualitative inquiry. Splits by speaker and conversation will precede threshold tuning. Evaluation will cover per-class errors, coverage, selective risk, caption latency, cue latency, and cue age.

A four- to six-person pilot will refine task difficulty, accessibility, fatigue management, and instrumentation. It will not establish efficacy. The main protocol will then freeze the cue pool, models, thresholds, materials, exclusions, and analysis. Display limits and cue lifetimes will reside in a versioned parameter sheet rather than undocumented implementation choices.

### Controlled evaluation

A counterbalanced within-participant study will provisionally recruit approximately 24 DHH adults. Final recruitment will be justified through precision or simulation-based planning over plausible participant and item variability, attrition, and capacity. Unstable pilot effects will not be treated as dependable power estimates. An insufficiently informative study will be reported as exploratory.

Participants will view matched prerecorded conversations through the head-worn interface. Different matched items will be assigned across conditions to reduce learning effects. Adaptive layouts will be explored in co-design and piloting, then the same caption algorithm, adaptation rules, timing, typography, and speaker mapping will be frozen across conditions. No separate causal claim about layout will follow:

| Condition | Supplementary information |
| --- | --- |
| C0: Captions only | No supplementary cues |
| C1: Ungated cues | All eligible low-stakes cues from the frozen pool, without optional uncertainty/load suppression |
| C2: Gated cues | The same pool filtered by the frozen presentation policy |

Both C1 and C2 retain hard validity, identity, and expiry checks. Ungated does not mean unsafe or obsolete output. Cue generation will be frozen rather than resampled between conditions.

The **primary outcome is interpretation accuracy on prespecified low-ambiguity items; C2 versus C0 is the primary contrast**. C2 versus C1 is a planned secondary contrast. Secondary measures include effort, discomfort, interruptions, cue exposure, and agency. Incorrect or stale cue probes will occupy a separately labelled secondary block, not contaminate primary accuracy items. Participants will know that assistance can be inaccurate and receive debriefing.

Mixed-effects analysis, or a prespecified alternative if observations are sparse, will account for participants and items. Estimates and uncertainty will accompany significance tests, with multiplicity addressed for secondary analyses. Non-significance will not imply equivalence or safety. Because gating changes cue density, C2 versus C1 estimates the net policy effect: it cannot isolate calibration from fewer interruptions. A rate-matched control is a later study.

### Optional live extension

If technical and comfort criteria are met, six to eight participants may undertake brief live conversations with consenting partners. Logs and participant-selected episode replay will examine attribution, stale prompts, repair, and social acceptability. Uncontrolled input quality will be documented. This extension supports feasibility and experience claims, not long-term participation or well-being effects.

## 5. Optional daily self-awareness module

RQ4 is a separate, non-critical-path pilot: approximately eight to twelve consenting adults over two weeks, subject to additional ethical approval and signal access. Participants will select one or two hand habits they wish to understand. Conditions may contrast manual reflection, HR plus activity context, and those inputs plus selected motor patterns. This small study will investigate feasibility rather than comparative efficacy.

MindSeed's exploratory fieldwork connects fidgeting data with personal reflection; Grippy illustrates both awareness and unwanted burden [LI-04, LI-05]. Neither validates an unconscious-action classifier. HR/HRV can diverge from experienced stress [HRV-01, HRV-02]. sEMG decoding of instructed computer gestures does not establish interpretation of arbitrary spontaneous behavior [EMG-01]. Whether an event was previously unnoticed requires the wearer's account, not a sensor-derived assertion.

Consumer Neural Band command events must not be presented as raw muscle recordings. Research access through Aria is a distinct pathway [META-03, META-04]. Apple Watch measurement, HealthKit storage, and application delivery timing require separate checks [APPLE-01, APPLE-02]. Without adequate access, the module will use manual reflection or approved research equipment, or be deferred. Evaluation will emphasize false prompts per hour, contextual interpretation, autonomy, and burden. Harmless fidgeting will not be something the system automatically tries to suppress.

## 6. Ethics, feasibility, and doctoral development

Institutional approval will precede recruitment. Everyone whose speech or image is processed must consent; uninvolved bystanders will not be analyzed. Runtime buffers will be bounded and minimized, with research recordings governed separately. The broader concept's 90-second buffer is not a mandatory retention target. Semantic summaries can remain sensitive even after footage is deleted.

Third-party processing requires institutional approval and applicable agreements. A provider's statement that inputs are not used for training does not establish zero retention [JEV-04]. Public artifacts will contain designs, synthetic examples, and permitted code—not participant recordings, physiological traces, identity embeddings, or credentials. Participants may pause or withdraw; discomfort or loss of usable access support triggers a break. No diagnostic or therapeutic claim is intended.

Months 1–2 will establish device feasibility, community relationships, and ethics; months 3–4 will support co-design; months 5–6 will deliver the replay prototype and offline analysis; month 7 will pilot and freeze the protocol; months 8–10 will conduct the main study; months 11–12 will analyze and write. Optional extensions can be postponed. Minimum success is a reproducible policy evaluation and grounded design reasoning, not product release or publication acceptance.

The project fits Dr Li's interest in situated interaction and human–wearable relationships [LI-00]. His CSCW 2026 work informs attention to differing stakeholder perspectives; Reminiscope informs participant-shaped AI experiences; MindSeed and the earlier Grippy motivate reflection and negotiable support [LI-02, LI-03, LI-04, LI-05]. These are methodological connections, not claims that findings transfer directly to DHH conversation. Supervision would strengthen participatory design, qualitative interpretation, and mixed-method evaluation. Expected contributions are a bounded design space, an auditable prototype, and evidence about when assistance helps, distracts, or should remain silent.

## Source references

Keys below resolve to explicit primary or official sources. The complete catalog, including the original proposal's 18 references and evidence limitations, is in [参考文献](../07-文献与证据/参考文献.md).

- [HCI-01] Peng et al. (2018). *SpeechBubbles*. https://doi.org/10.1145/3173574.3173867
- [HCI-02] Berke, Caulfield, and Huenerfauth (2017). *DHH Perspectives on Imperfect ASR*. https://doi.org/10.1145/3132525.3132541
- [HCI-03] de Lacerda Pataca et al. (2023). *Visualization of Speech Prosody and Emotion in Captions*. https://doi.org/10.1145/3544548.3581511
- [HCI-04] de Lacerda Pataca et al. (2025). *CuCap*. https://doi.org/10.1145/3663547.3746400
- [HCI-05] de Lacerda Pataca et al. (2026). *Fuzzy Feelings*. https://doi.org/10.1145/3772318.3793421
- [HCI-06] Wang et al. (2026). *VocalEyes*. Preprint. https://arxiv.org/abs/2609.32983
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
