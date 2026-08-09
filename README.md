# Figma Flutter Implementation Skill

[🇬🇧 English](#english) · [🇪🇬 العربية](#arabic)

<a id="english"></a>
<details open>
<summary><strong>🇬🇧 English</strong></summary>

## Overview

Converts a Figma screen to Flutter while respecting the active project's design system, assets, reusable widgets, feature structure, and UI-state conventions.

The workflow is progressive: it verifies the checkout, inventories the live project and Figma, proves reuse before creating anything, implements only approved scope, then verifies the result.

## Prerequisites

1. Install GitHub CLI and authenticate an account with access to this private repository:

   ```bash
   brew install gh
   gh auth login
   ```

2. Connect Figma MCP in Codex or Claude Code.
3. Open the correct Flutter project and branch before invoking the skill. No Flutter dependencies need to be added.

## Install

Run one command from a terminal:

```bash
git clone https://github.com/Sragsakr/figma-flutter-implementation-skill.git && cd figma-flutter-implementation-skill && ./install.sh both
```

Replace `both` with `codex` or `claude` to install one version only. The installer never overwrites an existing skill.

## Global availability

This is a personal, global installation: the installer copies the skill to the tool's user-level skills directory, so it is available in every project on this machine.

| Tool | Global location |
| --- | --- |
| Codex | `~/.codex/skills/figma-flutter-implementation/` |
| Claude Code | `~/.claude/skills/figma-flutter-implementation/` |

Install it once per machine. A fresh Claude Code session is needed after installation; open a new Codex task if the skill is not yet visible.

## Use

Start a fresh Claude Code session and invoke:

```text
/figma-flutter-implementation <Figma URL>
```

In Codex, send the Figma URL with a Flutter implementation request, or name the skill explicitly.

## Guarantees

- Audit real definitions and consumers before editing.
- Complete a widget reuse inventory for every Figma component.
- Reuse existing project tokens, asset accessors, responsive extensions, widgets, and state patterns.
- Do not add assets, dependencies, tokens, routes, shared components, or abstractions without explicit approval.
- Keep screen UI state separate from independent business logic.

</details>

<a id="arabic"></a>
<details>
<summary><strong>🇪🇬 العربية</strong></summary>

## الفكرة

تحوّل الـSkill شاشة Figma إلى Flutter مع الالتزام بالـdesign system والأصول والـWidgets والـfeature structure والـUI state المعتمدة فعليًا داخل المشروع.

الـworkflow تدريجي: يتحقق من الـcheckout، ويراجع Figma والمشروع، ويوثق إعادة الاستخدام قبل أي كود، وينفّذ النطاق الموافق عليه فقط، ثم يختبر الناتج.

## قبل الاستخدام

1. ثبّت GitHub CLI وسجّل دخولك بحساب له صلاحية على هذا الـrepository الخاص:

   ```bash
   brew install gh
   gh auth login
   ```

2. وصّل Figma MCP في Codex أو Claude Code.
3. افتح مشروع Flutter الصحيح وعلى الـbranch الصحيح قبل استدعاء الـSkill. لا تحتاج تضيف أي dependencies للمشروع.

## التثبيت

نفّذ أمرًا واحدًا من الـTerminal:

```bash
git clone https://github.com/Sragsakr/figma-flutter-implementation-skill.git && cd figma-flutter-implementation-skill && ./install.sh both
```

بدّل `both` إلى `codex` أو `claude` لو تريد نسخة واحدة فقط. الـInstaller لا يستبدل نسخة موجودة بالفعل.

## التثبيت العام لكل المشاريع

هذا التثبيت Personal وGlobal بالفعل: الـInstaller ينسخ الـSkill داخل مجلد الـSkills الخاص بالمستخدم، لذلك تكون متاحة تلقائيًا في كل مشروع على نفس الجهاز.

| الأداة | المسار العام |
| --- | --- |
| Codex | `~/.codex/skills/figma-flutter-implementation/` |
| Claude Code | `~/.claude/skills/figma-flutter-implementation/` |

تثبّتها مرة واحدة لكل جهاز. بعد التثبيت ابدأ Session جديدة في Claude Code؛ وفي Codex افتح Task جديدة إذا لم تظهر الـSkill فورًا.

## طريقة الاستخدام

ابدأ Session جديدة في Claude Code، ثم اكتب:

```text
/figma-flutter-implementation <Figma URL>
```

في Codex، ابعت رابط Figma مع طلب تنفيذ Flutter، أو اذكر اسم الـSkill صراحة.

## الضمانات

- يراجع التعريفات ومواضع الاستخدام الحقيقية قبل التعديل.
- يعمل Widget Reuse Inventory لكل Component في Figma.
- يعيد استخدام الـtokens والـasset accessors والـextensions والـWidgets والـstate patterns الموجودة.
- لا يضيف assets أو dependencies أو tokens أو routes أو shared components أو abstractions من دون موافقة صريحة.
- يفصل UI state الخاصة بالشاشة عن business logic المستقلة.

</details>
