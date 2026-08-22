# Figma Flutter Implementation Skill

> Evidence-driven Figma-to-Flutter creation, synchronization, and visual refinement that preserves the active project's design system and architecture.

[🇬🇧 English](#english) · [🇪🇬 العربية](#arabic)

---

<a id="english"></a>
<details open>
<summary><strong>🇬🇧 English documentation</strong></summary>

## Overview

This skill creates or updates Flutter screens and flows from Figma while respecting the active project's theme, assets, reusable widgets, feature structure, routing, localization, and state-management conventions.

It does not jump directly from a Figma URL to code. It first inspects Figma and the live project, proves reuse decisions, and publishes an evidence-backed **Implementation Contract**. Code changes start only after that contract is approved.

```text
Figma target + current Flutter project
                  ↓
        Discovery and reuse audit
                  ↓
     Build Tree or Change Tree + table
                  ↓
              Approval
                  ↓
        Controlled implementation
                  ↓
       Visual and behavioral verification
```

## Operation modes

| Mode | Use it when | Plan produced before editing |
| --- | --- | --- |
| `CREATE` | The screen or flow is not implemented | Build tree, Figma coverage, behavior/data/state mapping, architecture budget |
| `SYNC` | Flutter UI exists and Figma changed | Current-to-target change tree with additions, modifications, and safe removals |
| `REFINE` | A bounded visual/component adjustment is needed | Focused change contract limited to the selected scope |
| `ANALYZE` | You need an implementation plan only | Full contract with no file edits |

## How automatic mode detection works

If you provide only the skill name and a Figma URL, the skill does not guess from the URL. It determines the mode from Figma and project evidence:

1. Inspect the Figma target and classify it as a complete flow, screen, component, variant, or state.
2. Read its names, hierarchy, visible content, components, and prototype relationships.
3. Search the current project by routes, pages, symbols, visible/localized text, assets, feature entry points, and similar component consumers.
4. Choose the default mode:
   - Matching screen/flow implementation found → `SYNC`.
   - Existing implementation plus a bounded component/variant target → `REFINE`.
   - No matching implementation after evidence-based search → `CREATE`.
   - Explicit request for planning only → `ANALYZE`.
5. If multiple implementations match, the Figma scope is incomplete, or confidence is insufficient, ask one concise clarification instead of editing.

The detected mode and its evidence appear at the top of the Implementation Contract, so you can correct it before approving any code change.

## What the Implementation Contract includes

- Explicit scope and exclusions.
- A build tree for new UI or a change tree for existing UI.
- `ADD`, `MODIFY`, `REMOVE`, `REMOVE USAGE`, `REUSE`, `EXTEND`, `KEEP`, `BLOCKED`, and `UNCERTAIN` decisions.
- Figma-node and project-code evidence.
- Expected files, assets, routes, state, data, and tests.
- Separate destructive decisions for UI usage, source files, registrations, state, and business logic.
- Visual comparison and validation plan.

One approval authorizes all listed actions. If implementation reveals unplanned work, the skill pauses only that work and presents a focused **Plan Delta**.

## Prerequisites

1. Install GitHub CLI and authenticate an account with access to this private repository:

   ```bash
   brew install gh
   gh auth login
   ```

2. Connect Figma MCP in Codex or Claude Code.
3. Open the correct Flutter project and branch before invoking the skill.

No Flutter dependency is required merely to install the skill.

## Installation

Install both variants:

```bash
git clone https://github.com/Sragsakr/figma-flutter-implementation-skill.git \
  && cd figma-flutter-implementation-skill \
  && ./install.sh both
```

Use `./install.sh codex` or `./install.sh claude` to install one variant only. The installer intentionally refuses to overwrite an existing installation; rename or remove the installed copy before installing an update.

### Global locations

| Tool | Location |
| --- | --- |
| Codex | `~/.codex/skills/figma-flutter-implementation/` |
| Claude Code | `~/.claude/skills/figma-flutter-implementation/` |

Start a fresh Claude Code session after installation. Open a new Codex task if the skill is not immediately visible.

## Quick start

Claude Code:

```text
/figma-flutter-implementation <FIGMA_URL>
```

Codex: provide the Figma URL with a Flutter implementation request, or explicitly name `$figma-flutter-implementation`.

A short daily-use prompt is usually enough:

```text
/figma-flutter-implementation <FIGMA_URL>

Create or synchronize this design with the current Flutter project. Show me the Implementation Contract before editing, then execute only the approved actions.
```

## Prompt examples

### 1. Create a new screen

```text
/figma-flutter-implementation

Implement this new screen in the current Flutter project:
<FIGMA_URL>

Use CREATE mode. Reuse the existing theme, shell, routing, widgets, localization, and state patterns.

Before editing, show me:
- Scope and exclusions
- Build Tree
- Figma coverage
- Reuse and extension decisions
- State and data sources
- Assets and expected files
- Architecture budget
- Verification plan

Wait for my approval of the Implementation Contract.
```

### 2. Create a complete flow

```text
/figma-flutter-implementation

Implement the complete new flow from this Figma target:
<FIGMA_URL>

Inspect every screen, variant, state, and navigation relationship in scope. Reuse the project's existing app shell and business flows. Show one Build Tree for the whole flow and identify any behavior or data that Figma does not prove. Do not invent missing APIs, routes, or model fields.
```

### 3. Synchronize an existing screen after a Figma update

```text
/figma-flutter-implementation

This screen already exists in Flutter, but its full Figma design changed:
<FIGMA_URL>

Use SYNC mode. Establish the current implementation baseline, then show a Change Tree and action table covering:
- Additions
- In-place modifications
- Removed UI usage
- Items intentionally kept
- Shared consumers
- Assets, state, navigation, and tests

Do not treat removed UI as permission to delete shared source or business logic. Show the complete Change Contract before editing.
```

### 4. Synchronize an existing flow

```text
/figma-flutter-implementation

Synchronize the existing Flutter flow with the updated Figma flow:
<FIGMA_URL>

Group the Change Tree by screen. Preserve existing routes, shared components, business state, and assets unless the evidence and approved contract require a change. For every deletion, distinguish layout removal, usage removal, registration removal, file deletion, state deletion, and business deletion.
```

### 5. Refine one component only

```text
/figma-flutter-implementation

Update the existing settings header to match this Figma variant:
<FIGMA_URL>

Use REFINE mode. The rest of the screen, navigation, and business logic are out of scope. Inspect the shared header and its consumers before deciding whether to REUSE, EXTEND, or MODIFY it. Show a focused Change Contract before editing.
```

### 6. Analyze without changing files

```text
/figma-flutter-implementation

Analyze this Figma target against the current Flutter project:
<FIGMA_URL>

Use ANALYZE mode. Produce the discovery inventory, reuse mapping, Build/Change Tree, action table, expected files, gaps, risks, and verification plan. Do not modify any file.
```

### 7. Work from a partial Figma selection

```text
/figma-flutter-implementation

This URL points to a component or variant, not the complete screen:
<FIGMA_URL>

Change only the selected scope. Do not treat anything outside the selection as removed. Mark any decision that requires the full frame as UNCERTAIN and ask for the smallest missing input instead of guessing.
```

### 8. Request strict anti-hallucination behavior

```text
/figma-flutter-implementation

Implement this target:
<FIGMA_URL>

Use strict evidence mode:
- Add no UI that is absent from Figma, project conventions, or the approved contract.
- Do not infer navigation from a card's appearance.
- Do not invent APIs, model fields, production values, or business behavior.
- Treat Figma sample content as visual data only.
- Mark missing consequential evidence BLOCKED or UNCERTAIN.
- Show the Implementation Contract before editing.
```

## Approving the contract

Approve all listed work:

```text
I approve the complete Implementation Contract. Execute only the listed actions and present any unexpected work as a Plan Delta.
```

Approve with exclusions:

```text
I approve the contract except:
- AS-02: do not add the new asset yet.
- UI-07: keep the existing banner.
- ST-03: do not change business state.

Update the contract and proceed with the remaining approved actions.
```

Revise before execution:

```text
Revise the contract:
- Extend the existing shared card instead of creating a local duplicate.
- Keep the current route unchanged.
- Exclude tablet layout from this task.
- Do not delete orphan assets.

Show the final contract before editing.
```

Approve a newly discovered delta:

```text
I approve Plan Delta #1 only. Do not expand any other part of the scope.
```

## Guarantees

- Audits real definitions and consumers before editing.
- Reuses active tokens, asset accessors, responsive helpers, widgets, routes, localization, and state patterns.
- Maps meaningful Figma sections and states before creating UI.
- Does not invent UI, behavior, APIs, models, or production data from visual implication.
- Does not treat a partial frame as evidence for deleting the rest of a screen.
- Separates UI removal from shared-source, asset, state, navigation, and business deletion.
- Prevents unapproved additions and scope expansion through the contract and Plan Delta gates.
- Runs focused validation and reports remaining visual differences as intentional, blocked, or out of scope.

## Repository validation

Validate frontmatter, Markdown links, eval JSON, and Codex/Claude variant parity:

```bash
python3 scripts/validate_skill.py
```

</details>

---

<a id="arabic"></a>
<details>
<summary><strong>🇪🇬 التوثيق بالعربي</strong></summary>

## الفكرة

الـSkill تنشئ أو تعدّل شاشات وFlows في Flutter من Figma، مع الحفاظ على الـtheme والـassets والـshared widgets والـfeature structure والـrouting والـlocalization والـstate management المستخدمة فعليًا في المشروع.

الـSkill لا تنتقل مباشرة من رابط Figma إلى الكود. في البداية تراجع Figma والمشروع الحالي، وتثبت قرارات إعادة الاستخدام، ثم تعرض **Implementation Contract** مبنية على أدلة. تعديل الكود لا يبدأ إلا بعد الموافقة على العقد.

```text
Figma الجديدة + مشروع Flutter الحالي
                  ↓
      Discovery ومراجعة إعادة الاستخدام
                  ↓
       Build Tree أو Change Tree + جدول
                  ↓
               الموافقة
                  ↓
            تنفيذ داخل النطاق
                  ↓
        تحقق بصري وسلوكي من النتيجة
```

## أوضاع التشغيل

| الوضع | يُستخدم متى؟ | الخطة التي تظهر قبل التعديل |
| --- | --- | --- |
| `CREATE` | الشاشة أو الـFlow غير منفذة | Build Tree وFigma coverage ومصادر behavior/data/state وArchitecture Budget |
| `SYNC` | التنفيذ موجود وتصميم Figma اتغير | Change Tree من التنفيذ الحالي إلى المستهدف تشمل الإضافة والتعديل والحذف الآمن |
| `REFINE` | تعديل بصري أو Component داخل نطاق محدود | Change Contract مركزة على الجزء المطلوب فقط |
| `ANALYZE` | المطلوب تحليل وخطة فقط | Contract كاملة بدون تعديل ملفات |

## إزاي الـSkill تكتشف نوع التشغيل تلقائيًا؟

لو كتبت اسم الـSkill ورابط Figma فقط، فهي لا تخمّن النوع من الرابط نفسه، لكنها تحدده من أدلة Figma والمشروع:

1. تراجع Figma target وتحدد هل هي Flow كاملة أو Screen أو Component أو Variant أو State.
2. تقرأ الأسماء والـhierarchy والمحتوى الظاهر والـcomponents وعلاقات الـprototype.
3. تبحث في المشروع الحالي عن routes وpages وsymbols والنصوص الظاهرة أو المترجمة والـassets والـfeature entry points والـconsumers المشابهة.
4. تختار الوضع الافتراضي:
   - لقت تنفيذًا مطابقًا للشاشة أو الـFlow → `SYNC`.
   - لقت تنفيذًا موجودًا والرابط يشير إلى Component أو Variant محددة → `REFINE`.
   - لم تجد تنفيذًا مطابقًا بعد بحث مبني على أدلة → `CREATE`.
   - المستخدم طلب خطة فقط صراحة → `ANALYZE`.
5. لو ظهر أكثر من تنفيذ محتمل، أو Figma scope غير كاملة، أو الأدلة غير كافية، تسأل سؤالًا واحدًا مختصرًا بدل تعديل الكود بالتخمين.

الوضع المكتشف والأدلة الخاصة به يظهران في أول Implementation Contract، وبالتالي تقدر تصححه قبل الموافقة على أي تعديل.

## محتويات Implementation Contract

- النطاق وما هو خارج النطاق.
- Build Tree للـUI الجديدة أو Change Tree للتنفيذ الموجود.
- قرارات `ADD` و`MODIFY` و`REMOVE` و`REMOVE USAGE` و`REUSE` و`EXTEND` و`KEEP` و`BLOCKED` و`UNCERTAIN`.
- أدلة من Figma nodes ومن كود المشروع.
- الملفات والـassets والـroutes والـstate والبيانات والاختبارات المتوقعة.
- فصل الحذف من الـUI عن حذف source files أو registrations أو state أو business logic.
- خطة المقارنة البصرية والـvalidation.

موافقة واحدة تعتمد كل العناصر المدرجة. لو ظهر احتياج جديد أثناء التنفيذ، تتوقف الـSkill عن هذا الجزء فقط وتعرض **Plan Delta** محددة.

## قبل الاستخدام

1. ثبّت GitHub CLI وسجل الدخول بحساب له صلاحية على الـrepository الخاص:

   ```bash
   brew install gh
   gh auth login
   ```

2. وصّل Figma MCP في Codex أو Claude Code.
3. افتح مشروع Flutter الصحيح وعلى الـbranch المطلوب قبل تشغيل الـSkill.

تثبيت الـSkill نفسها لا يحتاج إضافة dependency إلى مشروع Flutter.

## التثبيت

لتثبيت نسختي Codex وClaude Code:

```bash
git clone https://github.com/Sragsakr/figma-flutter-implementation-skill.git \
  && cd figma-flutter-implementation-skill \
  && ./install.sh both
```

استخدم `./install.sh codex` أو `./install.sh claude` لتثبيت نسخة واحدة. الـinstaller يرفض استبدال نسخة مثبتة عمدًا؛ غيّر اسم النسخة الحالية أو احذفها قبل تثبيت تحديث.

### مسارات التثبيت العام

| الأداة | المسار |
| --- | --- |
| Codex | `~/.codex/skills/figma-flutter-implementation/` |
| Claude Code | `~/.claude/skills/figma-flutter-implementation/` |

ابدأ Session جديدة في Claude Code بعد التثبيت. وفي Codex افتح Task جديدة لو الـSkill لم تظهر مباشرة.

## الاستخدام السريع

في Claude Code:

```text
/figma-flutter-implementation <FIGMA_URL>
```

في Codex ابعت رابط Figma مع طلب تنفيذ Flutter، أو اذكر `$figma-flutter-implementation` صراحة.

في الاستخدام اليومي غالبًا يكفي:

```text
/figma-flutter-implementation <FIGMA_URL>

أنشئ أو زامن التصميم مع مشروع Flutter الحالي. اعرض Implementation Contract قبل تعديل الكود، وبعد موافقتي نفذ العناصر المعتمدة فقط.
```

## أمثلة Prompts

### 1. إنشاء شاشة جديدة

```text
/figma-flutter-implementation

نفذ الشاشة الجديدة دي داخل مشروع Flutter الحالي:
<FIGMA_URL>

استخدم CREATE mode. أعد استخدام الـtheme والـshell والـrouting والـwidgets والـlocalization والـstate patterns الموجودة.

قبل تعديل الكود اعرض:
- Scope وما هو خارج النطاق
- Build Tree
- Figma coverage
- قرارات REUSE وEXTEND
- مصادر الـstate والبيانات
- الـassets والملفات المتوقعة
- Architecture budget
- Verification plan

انتظر موافقتي على Implementation Contract.
```

### 2. إنشاء Flow كاملة

```text
/figma-flutter-implementation

نفذ الـFlow الجديدة كاملة من رابط Figma ده:
<FIGMA_URL>

راجع كل الشاشات والـvariants والـstates وعلاقات الـnavigation الموجودة داخل النطاق. أعد استخدام app shell والـbusiness flows الحالية. اعرض Build Tree واحدة للـFlow كاملة، وحدد أي behavior أو data لا تثبتها Figma. لا تخترع APIs أو routes أو model fields ناقصة.
```

### 3. مزامنة شاشة موجودة بعد تحديث Figma

```text
/figma-flutter-implementation

الشاشة دي منفذة بالفعل في Flutter، لكن التصميم الكامل اتغير على Figma:
<FIGMA_URL>

استخدم SYNC mode. سجل baseline للتنفيذ الحالي، ثم اعرض Change Tree وجدول Actions يوضح:
- الإضافات
- التعديلات على الموجود
- ما سيُزال من الـUI
- ما سيظل موجودًا
- كل shared consumers
- الـassets والـstate والـnavigation والاختبارات

لا تعتبر حذف UI تصريحًا بحذف shared source أو business logic. اعرض Change Contract كاملة قبل تعديل الملفات.
```

### 4. مزامنة Flow موجودة

```text
/figma-flutter-implementation

زامن الـFlow الموجودة في Flutter مع الـFlow المحدثة على Figma:
<FIGMA_URL>

قسّم Change Tree حسب كل شاشة. حافظ على الـroutes والـshared components والـbusiness state والـassets الحالية إلا لو الأدلة والعقد المعتمد يتطلبان تغييرها. في كل عملية حذف افصل بين إزالة layout وإزالة usage وإزالة registration وحذف الملف وحذف state وحذف business logic.
```

### 5. تعديل Component واحدة فقط

```text
/figma-flutter-implementation

عدّل settings header الحالية لتطابق Figma variant دي:
<FIGMA_URL>

استخدم REFINE mode. باقي الشاشة والـnavigation والـbusiness logic خارج النطاق. راجع الـshared header وكل consumers قبل قرار REUSE أو EXTEND أو MODIFY. اعرض Change Contract مختصرة قبل التعديل.
```

### 6. تحليل بدون تعديل ملفات

```text
/figma-flutter-implementation

حلل تصميم Figma ده مقابل مشروع Flutter الحالي:
<FIGMA_URL>

استخدم ANALYZE mode. اعرض discovery inventory وreuse mapping وBuild/Change Tree وجدول Actions والملفات المتوقعة والـgaps والمخاطر وخطة التحقق. ممنوع تعديل أي ملف.
```

### 7. التعامل مع Figma selection جزئية

```text
/figma-flutter-implementation

الرابط ده يشير إلى Component أو Variant فقط، وليس الشاشة الكاملة:
<FIGMA_URL>

عدّل النطاق المحدد فقط. لا تعتبر أي شيء خارج الـselection محذوفًا. صنّف أي قرار يحتاج full frame كـUNCERTAIN واطلب أقل معلومة ناقصة بدل التخمين.
```

### 8. تشغيل Anti-Hallucination بشكل صارم

```text
/figma-flutter-implementation

نفذ التصميم ده:
<FIGMA_URL>

استخدم strict evidence mode:
- لا تضف UI غير موجودة في Figma أو project conventions أو العقد المعتمد.
- لا تستنتج navigation من شكل Card.
- لا تخترع APIs أو model fields أو production values أو business behavior.
- اعتبر محتوى Figma التجريبي visual data فقط.
- صنّف الأدلة المهمة الناقصة كـBLOCKED أو UNCERTAIN.
- اعرض Implementation Contract قبل التعديل.
```

## الموافقة على العقد

الموافقة على كل العناصر:

```text
موافق على Implementation Contract بالكامل. نفذ العناصر المدرجة فقط، وأي احتياج جديد اعرضه كـPlan Delta.
```

الموافقة مع استثناءات:

```text
موافق على العقد باستثناء:
- AS-02: لا تضف الـasset الجديدة حاليًا.
- UI-07: حافظ على الـbanner الحالية.
- ST-03: لا تعدل business state.

حدّث العقد ونفذ باقي العناصر المعتمدة.
```

تعديل الخطة قبل التنفيذ:

```text
عدّل العقد كالتالي:
- وسّع الـshared card الحالية بدل إنشاء نسخة local.
- حافظ على الـroute الحالية بدون تغيير.
- استبعد tablet layout من المهمة.
- لا تحذف orphan assets.

اعرض العقد النهائي قبل تعديل الكود.
```

الموافقة على Delta جديدة:

```text
موافق على Plan Delta #1 فقط. لا توسع أي جزء آخر من النطاق.
```

## الضمانات

- تراجع التعريفات ومواضع الاستخدام الحقيقية قبل التعديل.
- تعيد استخدام الـtokens والـasset accessors والـresponsive helpers والـwidgets والـroutes والـlocalization والـstate patterns الفعلية.
- تربط الأقسام والـstates المهمة في Figma بالتنفيذ قبل إنشاء الـUI.
- لا تخترع UI أو behavior أو APIs أو models أو production data من الشكل فقط.
- لا تعتبر Frame جزئية دليلًا لحذف بقية الشاشة.
- تفصل حذف UI عن حذف shared source أو assets أو state أو navigation أو business logic.
- تمنع الإضافات وتوسيع النطاق غير المعتمد عن طريق Implementation Contract وPlan Delta.
- تنفذ validation مركزة وتسجل أي فرق بصري متبقٍ كفرق مقصود أو محجوب أو خارج النطاق.

## التحقق من الـrepository

لفحص frontmatter وروابط Markdown وeval JSON وتطابق نسختي Codex وClaude Code:

```bash
python3 scripts/validate_skill.py
```

</details>
