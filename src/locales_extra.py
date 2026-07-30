"""Additional UI locales: German, Italian, Portuguese, Spanish, Arabic, Mandarin, Russian."""

from __future__ import annotations

FOCUS_NAMES = {
    "de": {
        "BFA": "Burkina Faso",
        "TCD": "Tschad",
        "ETH": "Äthiopien",
        "MLI": "Mali",
        "NER": "Niger",
        "SOM": "Somalia",
        "SSD": "Südsudan",
        "SDN": "Sudan",
    },
    "it": {
        "BFA": "Burkina Faso",
        "TCD": "Ciad",
        "ETH": "Etiopia",
        "MLI": "Mali",
        "NER": "Niger",
        "SOM": "Somalia",
        "SSD": "Sud Sudan",
        "SDN": "Sudan",
    },
    "pt": {
        "BFA": "Burquina Faso",
        "TCD": "Chade",
        "ETH": "Etiópia",
        "MLI": "Mali",
        "NER": "Níger",
        "SOM": "Somália",
        "SSD": "Sudão do Sul",
        "SDN": "Sudão",
    },
    "es": {
        "BFA": "Burkina Faso",
        "TCD": "Chad",
        "ETH": "Etiopía",
        "MLI": "Malí",
        "NER": "Níger",
        "SOM": "Somalia",
        "SSD": "Sudán del Sur",
        "SDN": "Sudán",
    },
    "ar": {
        "BFA": "بوركينا فاسو",
        "TCD": "تشاد",
        "ETH": "إثيوبيا",
        "MLI": "مالي",
        "NER": "النيجر",
        "SOM": "الصومال",
        "SSD": "جنوب السودان",
        "SDN": "السودان",
    },
    "zh": {
        "BFA": "布基纳法索",
        "TCD": "乍得",
        "ETH": "埃塞俄比亚",
        "MLI": "马里",
        "NER": "尼日尔",
        "SOM": "索马里",
        "SSD": "南苏丹",
        "SDN": "苏丹",
    },
    "ru": {
        "BFA": "Буркина-Фасо",
        "TCD": "Чад",
        "ETH": "Эфиопия",
        "MLI": "Мали",
        "NER": "Нигер",
        "SOM": "Сомали",
        "SSD": "Южный Судан",
        "SDN": "Судан",
    },
}

# Shared methods / sources / ethics blocks reused inside COPY packs
_METHODS = {
    "de": """### So entstehen die Zahlen
- **Join-Schlüssel:** ISO3-Codes (keine Ländernamen in Klartext).
- **IPC:** HDX-Long-Datei → `Validity period == current` und `Phase == 3+`. Anteile kommen als 0–1 und werden zu Prozenten.
- **Vertreibung:** UNHCR-API mit `coa` + `cf_type=ISO`. Summe aus Flüchtlingen + Asylsuchenden + weiteren Personen **im Aufnahmeland**. Ohne `coa` liefert die API ein Weltaggregat.
- **Kinderschutz:** WHO GHO `MDG_0000000001`, letztes Jahr pro Fokusland.
- **Compound score:** illustrativer z-Score, kein offizieller Index.

Mehr in `docs/methods.md`.
""",
    "it": """### Come sono costruiti i numeri
- **Chiave di join:** codici ISO3 (mai i nomi dei paesi in chiaro).
- **IPC:** file lungo HDX → `Validity period == current` e `Phase == 3+`. Le quote arrivano come 0–1 e diventano percentuali.
- **Spostamento:** API UNHCR con `coa` + `cf_type=ISO`. Sommiamo rifugiati + richiedenti asilo + altre persone **ospitate** nel paese. Senza `coa` si ottiene un aggregato mondiale.
- **Sopravvivenza infantile:** WHO GHO `MDG_0000000001`, ultimo anno per paese focus.
- **Compound score:** mix illustrativo di z-score, non un indice ufficiale.

Dettagli in `docs/methods.md`.
""",
    "pt": """### Como os números são construídos
- **Chave de junção:** códigos ISO3 (nunca nomes de países por extenso).
- **IPC:** ficheiro longo HDX → `Validity period == current` e `Phase == 3+`. Quotas chegam como 0–1 e viram percentagens.
- **Deslocamento:** API ACNUR com `coa` + `cf_type=ISO`. Somamos refugiados + requerentes de asilo + outras pessoas **acolhidas** no país. Sem `coa` obtém-se um agregado mundial.
- **Sobrevivência infantil:** OMS GHO `MDG_0000000001`, último ano por país-alvo.
- **Compound score:** mistura ilustrativa de z-scores, não é um índice oficial.

Mais em `docs/methods.md`.
""",
    "es": """### Cómo se construyen las cifras
- **Clave de unión:** códigos ISO3 (nunca unimos por el nombre del país en texto).
- **IPC:** archivo largo de HDX → se conserva `Validity period == current` y `Phase == 3+`. Las proporciones llegan como 0-1 y se convierten en porcentajes para los gráficos.
- **Desplazamiento:** API de ACNUR con `coa` + `cf_type=ISO`. Sumamos refugiados + solicitantes de asilo + otras personas de interés **acogidas** en el país. Omitir `coa` devuelve un agregado mundial, un error común al usar la API.
- **Supervivencia infantil:** OMS GHO `MDG_0000000001`, último año disponible por país focal.
- **Puntaje compuesto:** una combinación ilustrativa de puntajes z solo para la conversación, no un índice oficial.

Más detalle en `docs/methods.md`.
""",
    "ar": """### كيف تُبنى الأرقام
- **مفتاح الربط:** رموز ISO3 (لا نربط أبداً بأسماء الدول نصياً).
- **IPC:** ملف HDX الطويل، مع الاحتفاظ بـ `Validity period == current` و `Phase == 3+`. تصل الحصص بصيغة رقمية من 0 إلى 1 وتتحول إلى نسب مئوية في الرسوم البيانية.
- **النزوح:** واجهة برمجة تطبيقات المفوضية باستخدام `coa` و `cf_type=ISO`. نجمع اللاجئين وطالبي اللجوء وسائر الأشخاص موضع الاهتمام **المستضافين** داخل البلد. حذف `coa` يُرجع مجموعاً عالمياً، وهو خطأ شائع عند استخدام هذه الواجهة.
- **بقاء الأطفال:** منظمة الصحة العالمية GHO، المؤشر `MDG_0000000001`، أحدث سنة متاحة لكل دولة مستهدفة.
- **الدرجة المركّبة:** مزيج توضيحي من الدرجات المعيارية z-score لأغراض النقاش فقط، وليست مؤشراً رسمياً.

مزيد من التفاصيل في `docs/methods.md`.
""",
    "zh": """### 指标如何构建
- **关联键：** ISO3 代码（绝不用国家全名关联）。
- **IPC：** HDX 长表 → 保留 `Validity period == current` 且 `Phase == 3+`。份额以 0–1 给出，再转为百分比。
- **流离失所：** UNHCR API，参数 `coa` + `cf_type=ISO`。合计难民 + 寻求庇护者 + 其他受关切者（**收容国**口径）。省略 `coa` 会得到全球合计。
- **儿童生存：** WHO GHO `MDG_0000000001`，各国最新年份。
- **综合分：** 仅供讨论的 z 分数组合 , ,  非正式指数。

详见 `docs/methods.md`。
""",
    "ru": """### Как считаются показатели
- **Ключ соединения:** коды ISO3 (не названия стран текстом).
- **IPC:** длинный файл HDX → `Validity period == current` и `Phase == 3+`. Доли приходят как 0–1 и переводятся в проценты.
- **Перемещение:** API УВКБ с `coa` + `cf_type=ISO`. Сумма беженцев + просителей убежища + прочих лиц **на территории страны убежища**. Без `coa` API отдаёт мировой итог.
- **Выживание детей:** ВОЗ GHO `MDG_0000000001`, последний год по стране.
- **Compound score:** иллюстративная сумма z-оценок, не официальный индекс.

Подробнее в `docs/methods.md`.
""",
}

_SOURCES = {
    "de": """### Datenquellen
- **IPC akute Ernährungsunsicherheit** auf [HDX](https://data.humdata.org/dataset/global-acute-food-insecurity-country-data)
- **UNHCR Population Statistics API**, aufgenommene Flüchtlinge, Asylsuchende, weitere Personen
- **WHO GHO**. Sterblichkeit unter 5 Jahren (`MDG_0000000001`)
""",
    "it": """### Fonti dei dati
- **IPC insicurezza alimentare acuta** su [HDX](https://data.humdata.org/dataset/global-acute-food-insecurity-country-data)
- **API statistiche di popolazione UNHCR**, rifugiati, richiedenti asilo e altre persone ospitate
- **WHO GHO**, mortalità sotto i 5 anni (`MDG_0000000001`)
""",
    "pt": """### Origem dos dados
- **IPC insegurança alimentar aguda** em [HDX](https://data.humdata.org/dataset/global-acute-food-insecurity-country-data)
- **API de estatísticas populacionais ACNUR**, refugiados, requerentes de asilo e outras pessoas acolhidas
- **OMS GHO**, mortalidade em menores de 5 anos (`MDG_0000000001`)
""",
    "es": """### De dónde vienen los datos
- **Inseguridad alimentaria aguda IPC** en [HDX](https://data.humdata.org/dataset/global-acute-food-insecurity-country-data)
- **API de estadísticas de población de ACNUR**, refugiados, solicitantes de asilo y otras personas de interés acogidas
- **OMS GHO**, mortalidad en menores de 5 años (`MDG_0000000001`)
""",
    "ar": """### من أين تأتي البيانات
- **انعدام الأمن الغذائي الحاد وفق IPC** على [HDX](https://data.humdata.org/dataset/global-acute-food-insecurity-country-data)
- **واجهة برمجة تطبيقات إحصاءات السكان لدى المفوضية**، اللاجئون المستضافون وطالبو اللجوء وسائر الأشخاص موضع الاهتمام
- **منظمة الصحة العالمية GHO**، معدل وفيات الأطفال دون الخامسة (`MDG_0000000001`)
""",
    "zh": """### 数据来源
- **IPC 急性粮食不安全**：[HDX](https://data.humdata.org/dataset/global-acute-food-insecurity-country-data)
- **UNHCR 人口统计 API**, 收容国内的难民、寻求庇护者及其他受关切者
- **WHO GHO**, 5 岁以下儿童死亡率（`MDG_0000000001`）
""",
    "ru": """### Источники данных
- **IPC острая продовольственная нестабильность** на [HDX](https://data.humdata.org/dataset/global-acute-food-insecurity-country-data)
- **API статистики населения УВКБ**, беженцы, просители убежища и прочие лица на территории страны
- **ВОЗ GHO**, смертность детей до 5 лет (`MDG_0000000001`)
""",
}

_ETHICS = {
    "de": """### Sorgfalt & Grenzen
- Nur öffentliche Aggregate, keine Identifikation von Gemeinden oder Personen
- Landeswerte verbergen Hotspots; Zielhilfe nicht allein über diese Seite
- **Portfolio-Lernprojekt**, kein Produkt von OCHA / UNICEF / UNHCR

Ausführlicher: `docs/limitations.md`.
""",
    "it": """### Cura e limiti
- Solo aggregati pubblici, nessun tentativo di identificare comunità o individui
- I totali nazionali nascondono i hotspot; non destinare aiuti solo da questa pagina
- **Progetto di portfolio didattico**, non un prodotto OCHA / UNICEF / UNHCR

Dettagli in `docs/limitations.md`.
""",
    "pt": """### Cuidado e limites
- Apenas agregados públicos, sem tentar identificar comunidades ou indivíduos
- Totais nacionais escondem hotspots; não direcione ajuda só com esta página
- **Projeto de portfolio de aprendizagem**, não um produto OCHA / UNICEF / ACNUR

Mais em `docs/limitations.md`.
""",
    "es": """### Cuidado y límites
- Solo agregados públicos, sin ningún intento de identificar comunidades o individuos
- Los totales nacionales ocultan focos críticos; no dirija ayuda basándose solo en esta página
- Este es un **proyecto de portafolio de aprendizaje**, no un producto de OCHA / UNICEF / ACNUR

Hoja de límites más detallada: `docs/limitations.md`.
""",
    "ar": """### العناية والحدود
- تُستخدم فقط بيانات مجمّعة وعلنية، دون أي محاولة لتحديد هوية مجتمعات أو أفراد
- الإجماليات الوطنية تُخفي البؤر الساخنة، فلا تُوجَّه المساعدات استناداً إلى هذه الصفحة وحدها
- هذا **مشروع حافظة تعليمية**، وليس منتجاً تابعاً لمكتب تنسيق الشؤون الإنسانية أو اليونيسف أو المفوضية

ورقة أكثر تفصيلاً حول الحدود: `docs/limitations.md`.
""",
    "zh": """### 审慎与边界
- 仅使用公开汇总数据, 不识别社区或个人
- 国家级总量掩盖热点；请勿仅凭本页做援助瞄准
- 本工具为**学习型作品集项目**，非 OCHA / UNICEF / UNHCR 业务产品

详见 `docs/limitations.md`。
""",
    "ru": """### Осторожность и пределы
- Только публичные агрегаты, без идентификации общин или лиц
- Национальные итоги скрывают очаги; не используйте эту страницу для точечного распределения помощи
- **Учебный портфолио-проект**, не продукт УСГД / ЮНИСЕФ / УВКБ

Подробнее: `docs/limitations.md`.
""",
}


def _pack(
    *,
    lang_label: str,
    sidebar_hint: str,
    sidebar_guide: str,
    reset_view: str,
    status_ready: str,
    load_error: str,
    kpi_ipc_help: str,
    kpi_disp_help: str,
    kpi_u5_help: str,
    eyebrow: str,
    title: str,
    why: str,
    def_expander: str,
    def_title: str,
    def_body: str,
    kpi_ipc: str,
    kpi_disp: str,
    kpi_u5: str,
    nav_label: str,
    nav_story: str,
    nav_map: str,
    nav_country: str,
    nav_about: str,
    insight_title: str,
    action_heading: str,
    action_dual_pressure: str,
    action_missing_ipc: str,
    action_single_axis: str,
    country_select: str,
    trends_title: str,
    trends_intro: str,
    footer: str,
    demo_note: str,
    demo_watch: str,
    access_dates: str,
    access_dates_hint: str,
    loading: str,
    no_data: str,
    map_takeaway: str,
    trends_caption: str,
    about_intro: str,
    glossary_heading: str,
    access_date_label: str,
    chart_map_title: str,
    chart_map_pct: str,
    chart_map_people: str,
    chart_map_disp: str,
    chart_map_u5: str,
    chart_map_colorbar: str,
    chart_scatter_title: str,
    chart_scatter_x: str,
    chart_scatter_y: str,
    chart_scatter_u5: str,
    chart_drill_p1: str,
    chart_drill_p2: str,
    chart_drill_p3: str,
    chart_drill_bar_ipc: str,
    chart_drill_bar_disp: str,
    chart_drill_median: str,
    chart_drill_title: str,
    chart_no_data: str,
    chart_trends_p1: str,
    chart_trends_p2: str,
    chart_trends_series_disp: str,
    chart_trends_series_u5: str,
    chart_trends_title: str,
    country_gap: str,
    country_snapshot: str,
    insight_headline: str,
    insight_headline_empty: str,
    insight_contrast: str,
    insight_gap: str,
    insight_body_lead: str,
    map_gap_note: str,
    methods_md: str,
    sources_md: str,
    ethics_md: str,
) -> dict[str, str]:
    return {
        "lang_label": lang_label,
        "sidebar_hint": sidebar_hint,
        "sidebar_guide": sidebar_guide,
        "reset_view": reset_view,
        "status_ready": status_ready,
        "load_error": load_error,
        "kpi_ipc_help": kpi_ipc_help,
        "kpi_disp_help": kpi_disp_help,
        "kpi_u5_help": kpi_u5_help,
        "eyebrow": eyebrow,
        "title": title,
        "why": why,
        "def_expander": def_expander,
        "def_title": def_title,
        "def_body": def_body,
        "kpi_ipc": kpi_ipc,
        "kpi_disp": kpi_disp,
        "kpi_u5": kpi_u5,
        "nav_label": nav_label,
        "nav_story": nav_story,
        "nav_map": nav_map,
        "nav_country": nav_country,
        "nav_about": nav_about,
        "insight_title": insight_title,
        "action_heading": action_heading,
        "action_dual_pressure": action_dual_pressure,
        "action_missing_ipc": action_missing_ipc,
        "action_single_axis": action_single_axis,
        "country_select": country_select,
        "trends_title": trends_title,
        "trends_intro": trends_intro,
        "footer": footer,
        "demo_note": demo_note,
        "demo_watch": demo_watch,
        "access_dates": access_dates,
        "access_dates_hint": access_dates_hint,
        "loading": loading,
        "no_data": no_data,
        "map_takeaway": map_takeaway,
        "trends_caption": trends_caption,
        "about_intro": about_intro,
        "glossary_heading": glossary_heading,
        "methods_md": methods_md,
        "sources_md": sources_md,
        "access_date_label": access_date_label,
        "ethics_md": ethics_md,
        "chart_map_title": chart_map_title,
        "chart_map_pct": chart_map_pct,
        "chart_map_people": chart_map_people,
        "chart_map_disp": chart_map_disp,
        "chart_map_u5": chart_map_u5,
        "chart_map_colorbar": chart_map_colorbar,
        "chart_scatter_title": chart_scatter_title,
        "chart_scatter_x": chart_scatter_x,
        "chart_scatter_y": chart_scatter_y,
        "chart_scatter_u5": chart_scatter_u5,
        "chart_drill_p1": chart_drill_p1,
        "chart_drill_p2": chart_drill_p2,
        "chart_drill_p3": chart_drill_p3,
        "chart_drill_bar_ipc": chart_drill_bar_ipc,
        "chart_drill_bar_disp": chart_drill_bar_disp,
        "chart_drill_median": chart_drill_median,
        "chart_drill_title": chart_drill_title,
        "chart_no_data": chart_no_data,
        "chart_trends_p1": chart_trends_p1,
        "chart_trends_p2": chart_trends_p2,
        "chart_trends_series_disp": chart_trends_series_disp,
        "chart_trends_series_u5": chart_trends_series_u5,
        "chart_trends_title": chart_trends_title,
        "country_gap": country_gap,
        "country_snapshot": country_snapshot,
        "insight_headline": insight_headline,
        "insight_headline_empty": insight_headline_empty,
        "insight_contrast": insight_contrast,
        "insight_gap": insight_gap,
        "insight_body_lead": insight_body_lead,
        "map_gap_note": map_gap_note,
    }


COPY = {
    "de": _pack(
        lang_label="Sprache",
        sidebar_hint="Sprache jederzeit wechseln, die ganze Seite folgt.",
        sidebar_guide="Beginnen Sie mit **Story**, das ist die Kernbotschaft. Karte und Land sind optionale Zooms.",
        reset_view="Zurück zur Story",
        status_ready="Analysetabelle geladen",
        load_error="Analysetabelle nicht lesbar: {detail}. Führen Sie `python -m src.run_pipeline` aus und aktualisieren Sie.",
        kpi_ipc_help="Menschen in IPC-Phase 3+ (Krise oder schlimmer) in den acht Fokusländern mit aktueller nationaler Schätzung.",
        kpi_disp_help="Flüchtlinge + Asylsuchende + weitere Personen im Aufnahmeland (UNHCR).",
        kpi_u5_help="Median der WHO-Sterblichkeit unter 5 Jahren (pro 1.000 Lebendgeburten) im Fokuspanel.",
        eyebrow="Humanitäres Datenportfolio",
        title="Wo Bedarfe sich überlagern",
        why=(
            "Hunger, Vertreibung und Kindersterblichkeitsrisiko treten selten allein auf. "
            "Dieses Dashboard zeigt, wo diese Drücke sich verdichten, damit Prioritäten Menschen folgen, nicht Silos."
        ),
        def_expander="Wie wir Vertreibung zählen (kurz)",
        def_title="Festgelegte Definition",
        def_body=(
            "Personen **aufgenommen** im Asylland: Flüchtlinge + Asylsuchende + "
            "weitere Personen von Belang (UNHCR). Herkunftszahlen bleiben bewusst außen vor."
        ),
        kpi_ipc="In IPC-Phase 3+ (Fokusländer)",
        kpi_disp="Aufgenommene Vertriebene",
        kpi_u5="Median Sterblichkeit <5 Jahre",
        nav_label="Wohin möchten Sie schauen?",
        nav_story="Story",
        nav_map="Karte",
        nav_country="Ein Land",
        nav_about="Hinter den Zahlen",
        insight_title="Auf den Punkt",
        action_heading="Als Nächstes ansehen",
        action_dual_pressure=(
            "**{countries}** liegen bei IPC-Schwere und Aufnahme über dem Median, "
            "Ernährungssicherheit und Schutz vor der Priorisierung nebeneinander legen."
        ),
        action_missing_ipc=(
            "**{countries}**: keine aktuelle nationale IPC-Phase-3+-Schätzung in dieser Tabelle, "
            "leere Kartenfelder bedeuten unbekannt, nicht geringes Risiko."
        ),
        action_single_axis=(
            "Länder, die nur auf einer Achse auffallen (siehe Kontrast oben), "
            "verdienen trotzdem einen gezielten Blick, nicht nur die Doppeldruck-Gruppe."
        ),
        country_select="Land wählen",
        trends_title="Wie sich die Lage entwickelt",
        trends_intro="Dasselbe Land, etwas mehr Zeitkontext. Aufnahme und Kindersterblichkeit.",
        footer="Lernportfolio für humanitäre Datenrollen · Nicht für operative Entscheidungen",
        demo_note="90-Sekunden-Walkthrough",
        demo_watch="Demo öffnen",
        access_dates="Datenstand",
        access_dates_hint=",  Quellen unter Hinter den Zahlen",
        loading="Analysetabelle wird geladen …",
        no_data=(
            "Noch keine Analysetabelle: Pipeline einmal ausführen, dann aktualisieren.\n\n"
            "Im Projektordner:\n\n```bash\npython -m src.run_pipeline\n```\n\nDann Seite neu laden."
        ),
        map_takeaway=(
            "Dunkler = höherer Anteil in IPC-Phase 3+ (Krise oder schlimmer). "
            "Nutzen Sie dies als Schweregrad-Hintergrund vor der Story."
        ),
        trends_caption=(
            "Kurven aus UNHCR-Aufnahmehistorie und WHO-Sterblichkeit unter 5. "
            "IPC-Bewertungen kommen nicht monatlich, wir erfinden keinen glatten Hunger-Trend."
        ),
        about_intro="Für alle, die unter die Haube schauen wollen. Methoden, Glossar, Quellen, Grenzen.",
        glossary_heading="### Bewusst gewählte Begriffe",
        access_date_label="Abgerufen am",
        chart_map_title="Akute Ernährungsunsicherheit (IPC-Phase 3+). Fokusländer",
        chart_map_pct="IPC-Phase 3+ (%)",
        chart_map_people="Menschen in Phase 3+",
        chart_map_disp="Vertriebene (aufgenommen)",
        chart_map_u5="Sterblichkeit <5",
        chart_map_colorbar="% in Phase 3+",
        chart_scatter_title="Wo Vertreibung und Hunger zusammentreffen",
        chart_scatter_x="Aufgenommene Vertriebene (UNHCR)",
        chart_scatter_y="Bevölkerung in IPC-Phase 3+ (%)",
        chart_scatter_u5="Sterblichkeit <5 (pro 1000)",
        chart_drill_p1="Menschen in IPC-Phase 3+",
        chart_drill_p2="Aufgenommene Vertriebene",
        chart_drill_p3="Sterblichkeit <5 vs. Panel-Median",
        chart_drill_bar_ipc="Phase 3+",
        chart_drill_bar_disp="Vertriebene",
        chart_drill_median="Panel-Median",
        chart_drill_title="{country} auf einen Blick",
        chart_no_data="Noch nichts für {iso3}",
        chart_trends_p1="Aufnahme (UNHCR)",
        chart_trends_p2="Sterblichkeit <5 (WHO)",
        chart_trends_series_disp="Aufgenommene Vertriebene",
        chart_trends_series_u5="U5MR",
        chart_trends_title="{country} in den letzten Jahren",
        country_gap=(
            "Für {country} fehlt in diesem Extrakt eine aktuelle nationale IPC-Phase-3+-Schätzung. "
            "Das heißt nicht „kein Hunger“, nur, dass dieser öffentliche Ausschnitt still ist."
        ),
        country_snapshot=(
            "In {country} liegen etwa **{pct}%** der bewerteten Bevölkerung in Phase 3+, "
            "mit **{displaced}** aufgenommenen Vertriebenen und einer Sterblichkeit unter 5 "
            "von etwa **{u5mr}** pro 1.000 Lebendgeburten."
        ),
        insight_headline=(
            "Höchster Doppeldruck: {names} liegen bei oder über den Panel-Medianen "
            "für IPC-Phase-3+-Anteil ({ipc_pct}%) und aufgenommene Vertriebene ({displaced} Personen)."
        ),
        insight_headline_empty="Kein Land liegt in diesem Extrakt über beiden Medianen.",
        insight_contrast=(
            " Hinweis: {country} hat hohe Phase 3+ ({ipc_pct}%), aber geringere Aufnahme, "
            "Hunger und Aufnahme sind unterschiedliche Signale."
        ),
        insight_gap=(
            " Lücke: {names} {verb} keine aktuelle IPC-Phase-3+-Zeile hier, "
            "fehlende Daten, nicht null Bedarf."
        ),
        insight_body_lead=(
            "Für Programmteams: mit der Doppeldruck-Gruppe starten, dann "
            "Ernährungssicherheit und Schutz gemeinsam besprechen."
        ),
        map_gap_note=(
            "**Fehlendes IPC auf der Karte ist Absicht.** {names} {verb} keine *aktuelle* "
            "nationale Phase-3+-Zeile in diesem Extrakt. Das ist eine Abdeckungslücke, "
            "kein Nachweis, dass Hunger fehlt."
        ),
        methods_md=_METHODS["de"],
        sources_md=_SOURCES["de"],
        ethics_md=_ETHICS["de"],
    ),
    "it": _pack(
        lang_label="Lingua",
        sidebar_hint="Cambia lingua in qualsiasi momento. Tutta la pagina segue.",
        sidebar_guide="Inizia da **Story**, è il messaggio principale. Mappa e Paese sono zoom opzionali.",
        reset_view="Torna a Story",
        status_ready="Tabella di analisi caricata",
        load_error="Impossibile aprire la tabella di analisi: {detail}. Esegui `python -m src.run_pipeline`, poi aggiorna.",
        kpi_ipc_help="Persone in fase IPC 3+ (Crisi o peggio) nei otto paesi focus con stima nazionale corrente.",
        kpi_disp_help="Rifugiati + richiedenti asilo + altre persone ospitate nel paese di asilo (UNHCR).",
        kpi_u5_help="Mediana WHO della mortalità sotto i 5 anni (per 1.000 nati vivi) sul panel.",
        eyebrow="Portfolio di dati umanitari",
        title="Dove i bisogni si sovrappongono",
        why=(
            "Fame, spostamento e rischio per la sopravvivenza infantile raramente arrivano da soli. "
            "Questa dashboard mostra dove queste pressioni si accumulano, così le priorità seguono le persone, non i silos."
        ),
        def_expander="Come contiamo lo spostamento (breve)",
        def_title="Definizione fissata",
        def_body=(
            "Persone **ospitate** nel paese di asilo: rifugiati + richiedenti asilo + "
            "altre persone di competenza UNHCR. I conteggi per origine restano fuori di proposito."
        ),
        kpi_ipc="In fase IPC 3+ (paesi focus)",
        kpi_disp="Sfollati ospitati",
        kpi_u5="Mediana mortalità <5 anni",
        nav_label="Dove vuoi guardare?",
        nav_story="Story",
        nav_map="Mappa",
        nav_country="Un paese",
        nav_about="Dietro i numeri",
        insight_title="In parole semplici",
        action_heading="Cosa guardare dopo",
        action_dual_pressure=(
            "**{countries}** sono alti sia sulla severità IPC sia sull’ospitalità, "
            "allineare sicurezza alimentare e protezione prima di scegliere dove agire."
        ),
        action_missing_ipc=(
            "**{countries}**: nessuna stima nazionale IPC Fase 3+ attuale in questa tabella, "
            "una cella vuota sulla mappa significa sconosciuto, non basso rischio."
        ),
        action_single_axis=(
            "I paesi urgenti su una sola dimensione (vedi il contrasto sopra) "
            "meritano comunque uno sguardo mirato, non solo il gruppo a doppia pressione."
        ),
        country_select="Scegli un paese",
        trends_title="Come si è mosso il quadro",
        trends_intro="Stesso paese, un po’ più di contesto temporale, ospitalità e mortalità infantile.",
        footer="Portfolio formativo per ruoli dati umanitari · Non per decisioni operative",
        demo_note="Walkthrough di 90 secondi",
        demo_watch="Apri demo",
        access_dates="Dati estratti il",
        access_dates_hint=",  fonti in Dietro i numeri",
        loading="Sto caricando la tabella di analisi…",
        no_data=(
            "Nessuna tabella di analisi ancora, esegui una pipeline pulita, poi aggiorna.\n\n"
            "Dalla cartella del progetto:\n\n```bash\npython -m src.run_pipeline\n```\n\nPoi ricarica la pagina."
        ),
        map_takeaway=(
            "Più scuro = quota più alta in fase IPC 3+ (Crisi o peggio). "
            "Usalo come sfondo di severità prima di tornare a Story."
        ),
        trends_caption=(
            "Le curve vengono dallo storico di ospitalità UNHCR e dalla mortalità <5 WHO. "
            "Le valutazioni IPC non arrivano ogni mese, non inventiamo un trend falso."
        ),
        about_intro="Per chi vuole guardare sotto il cofano, metodi, glossario, fonti e limiti.",
        glossary_heading="### Parole scelte di proposito",
        access_date_label="Estratti il",
        chart_map_title="Insicurezza alimentare acuta (IPC fase 3+), paesi focus",
        chart_map_pct="IPC fase 3+ (%)",
        chart_map_people="Persone in fase 3+",
        chart_map_disp="Sfollati (ospitati)",
        chart_map_u5="Mortalità <5",
        chart_map_colorbar="% in fase 3+",
        chart_scatter_title="Dove spostamento e fame si incontrano",
        chart_scatter_x="Sfollati ospitati (UNHCR)",
        chart_scatter_y="Popolazione in fase IPC 3+ (%)",
        chart_scatter_u5="Mortalità <5 (per 1000)",
        chart_drill_p1="Persone in fase IPC 3+",
        chart_drill_p2="Sfollati ospitati",
        chart_drill_p3="Mortalità <5 vs mediana del panel",
        chart_drill_bar_ipc="Fase 3+",
        chart_drill_bar_disp="Sfollati",
        chart_drill_median="Mediana panel",
        chart_drill_title="{country} in sintesi",
        chart_no_data="Niente ancora per {iso3}",
        chart_trends_p1="Ospitalità (UNHCR)",
        chart_trends_p2="Mortalità <5 (WHO)",
        chart_trends_series_disp="Sfollati ospitati",
        chart_trends_series_u5="U5MR",
        chart_trends_title="{country} negli anni recenti",
        country_gap=(
            "Non troviamo una stima nazionale corrente IPC fase 3+ per {country} in questo estratto. "
            "Non significa «niente fame», solo che questa fetta di dati pubblici è silenziosa."
        ),
        country_snapshot=(
            "In {country}, circa **{pct}%** della popolazione valutata è in fase 3+, "
            "con **{displaced}** sfollati ospitati e mortalità sotto i 5 anni intorno a "
            "**{u5mr}** per 1.000 nati vivi."
        ),
        insight_headline=(
            "Doppia pressione più alta: {names} sono al o sopra le mediane del panel "
            "per quota IPC fase 3+ ({ipc_pct}%) e sfollati ospitati ({displaced} persone)."
        ),
        insight_headline_empty="Nessun paese supera entrambe le mediane in questo estratto.",
        insight_contrast=(
            " Nota: {country} ha fase 3+ alta ({ipc_pct}%) ma ospitalità più bassa, "
            "fame e accoglienza sono segnali diversi."
        ),
        insight_gap=(
            " Lacuna: {names} {verb} nessuna riga IPC fase 3+ corrente qui, "
            "dato mancante, non bisogno zero."
        ),
        insight_body_lead=(
            "Per i team di programma: partire dal gruppo a doppia pressione, "
            "poi discutere insieme sicurezza alimentare e protezione."
        ),
        map_gap_note=(
            "**IPC mancante sulla mappa è intenzionale.** {names} {verb} nessuna riga nazionale "
            "*corrente* in fase 3+ in questo estratto. È una lacuna di copertura, "
            "non prova che la fame sia assente."
        ),
        methods_md=_METHODS["it"],
        sources_md=_SOURCES["it"],
        ethics_md=_ETHICS["it"],
    ),
    "pt": _pack(
        lang_label="Idioma",
        sidebar_hint="Mude de idioma a qualquer momento. Toda a página segue.",
        sidebar_guide="Comece em **Story**, é a mensagem principal. Mapa e País são zooms opcionais.",
        reset_view="Voltar a Story",
        status_ready="Tabela de análise carregada",
        load_error="Não foi possível abrir a tabela de análise: {detail}. Execute `python -m src.run_pipeline` e atualize.",
        kpi_ipc_help="Pessoas em fase IPC 3+ (Crise ou pior) nos oito países-alvo com estimativa nacional atual.",
        kpi_disp_help="Refugiados + requerentes de asilo + outras pessoas acolhidas no país de asilo (ACNUR).",
        kpi_u5_help="Mediana OMS da mortalidade em menores de 5 anos (por 1.000 nados-vivos) no painel.",
        eyebrow="Portfolio de dados humanitários",
        title="Onde as necessidades se sobrepõem",
        why=(
            "Fome, deslocamento e risco para a sobrevivência infantil raramente aparecem sozinhos. "
            "Este painel mostra onde essas pressões se acumulam, para que as prioridades sigam pessoas, não silos."
        ),
        def_expander="Como contamos o deslocamento (rápido)",
        def_title="Definição fixada",
        def_body=(
            "Pessoas **acolhidas** no país de asilo: refugiados + requerentes de asilo + "
            "outras pessoas sob mandato do ACNUR. Contagens por origem ficam de fora de propósito."
        ),
        kpi_ipc="Em fase IPC 3+ (países-alvo)",
        kpi_disp="Deslocados acolhidos",
        kpi_u5="Mediana mortalidade <5 anos",
        nav_label="Onde quer olhar?",
        nav_story="Story",
        nav_map="Mapa",
        nav_country="Um país",
        nav_about="Por trás dos números",
        insight_title="Em linguagem clara",
        action_heading="O que ver a seguir",
        action_dual_pressure=(
            "**{countries}** estão altos tanto na severidade IPC como no acolhimento, "
            "alinhar segurança alimentar e proteção antes de escolher onde agir primeiro."
        ),
        action_missing_ipc=(
            "**{countries}**: sem estimativa nacional IPC Fase 3+ atual nesta tabela, "
            "célula vazia no mapa significa desconhecido, não baixo risco."
        ),
        action_single_axis=(
            "Países urgentes numa só dimensão (ver o contraste acima) "
            "ainda merecem um olhar específico, não só o conjunto de dupla pressão."
        ),
        country_select="Escolher um país",
        trends_title="Como o quadro tem evoluído",
        trends_intro="O mesmo país, um pouco mais de contexto temporal, acolhimento e mortalidade infantil.",
        footer="Portfolio de aprendizagem para funções de dados humanitários · Não para decisões operacionais",
        demo_note="Walkthrough de 90 segundos",
        demo_watch="Abrir demo",
        access_dates="Dados extraídos em",
        access_dates_hint=",  fontes em Por trás dos números",
        loading="A carregar a tabela de análise…",
        no_data=(
            "Ainda sem tabela de análise, execute um pipeline limpo e atualize.\n\n"
            "Na pasta do projeto:\n\n```bash\npython -m src.run_pipeline\n```\n\nDepois recarregue a página."
        ),
        map_takeaway=(
            "Mais escuro = maior percentagem em fase IPC 3+ (Crise ou pior). "
            "Use isto como fundo de severidade antes de voltar a Story."
        ),
        trends_caption=(
            "As curvas vêm do histórico de acolhimento ACNUR e da mortalidade <5 da OMS. "
            "As avaliações IPC não chegam todos os meses, não inventamos uma tendência falsa."
        ),
        about_intro="Para quem quer olhar por baixo do capô, métodos, glossário, fontes e limites.",
        glossary_heading="### Palavras escolhidas de propósito",
        access_date_label="Extraídos em",
        chart_map_title="Insegurança alimentar aguda (IPC fase 3+), países-alvo",
        chart_map_pct="IPC fase 3+ (%)",
        chart_map_people="Pessoas em fase 3+",
        chart_map_disp="Deslocados (acolhidos)",
        chart_map_u5="Mortalidade <5",
        chart_map_colorbar="% em fase 3+",
        chart_scatter_title="Onde deslocamento e fome se encontram",
        chart_scatter_x="Deslocados acolhidos (ACNUR)",
        chart_scatter_y="População em fase IPC 3+ (%)",
        chart_scatter_u5="Mortalidade <5 (por 1000)",
        chart_drill_p1="Pessoas em fase IPC 3+",
        chart_drill_p2="Deslocados acolhidos",
        chart_drill_p3="Mortalidade <5 vs mediana do painel",
        chart_drill_bar_ipc="Fase 3+",
        chart_drill_bar_disp="Deslocados",
        chart_drill_median="Mediana do painel",
        chart_drill_title="{country} em resumo",
        chart_no_data="Nada ainda para {iso3}",
        chart_trends_p1="Acolhimento (ACNUR)",
        chart_trends_p2="Mortalidade <5 (OMS)",
        chart_trends_series_disp="Deslocados acolhidos",
        chart_trends_series_u5="U5MR",
        chart_trends_title="{country} nos anos recentes",
        country_gap=(
            "Não encontrámos estimativa nacional atual IPC fase 3+ para {country} neste extrato. "
            "Isso não significa «sem fome», apenas que esta fatia de dados públicos está silenciosa."
        ),
        country_snapshot=(
            "Em {country}, cerca de **{pct}%** da população avaliada está em fase 3+, "
            "com **{displaced}** deslocados acolhidos e mortalidade em menores de 5 anos "
            "cerca de **{u5mr}** por 1.000 nados-vivos."
        ),
        insight_headline=(
            "Maior dupla pressão: {names} estão no ou acima das medianas do painel "
            "para quota IPC fase 3+ ({ipc_pct}%) e deslocados acolhidos ({displaced} pessoas)."
        ),
        insight_headline_empty="Nenhum país fica acima das duas medianas neste extrato.",
        insight_contrast=(
            " Nota: {country} tem fase 3+ alta ({ipc_pct}%) mas acolhimento mais baixo, "
            "fome e acolhimento são sinais diferentes."
        ),
        insight_gap=(
            " Lacuna: {names} {verb} linha IPC fase 3+ atual aqui, "
            "dado em falta, não necessidade zero."
        ),
        insight_body_lead=(
            "Para as equipas de programa: comece pelo grupo de dupla pressão, "
            "depois fale segurança alimentar e proteção em conjunto."
        ),
        map_gap_note=(
            "**IPC em falta no mapa é intencional.** {names} {verb} linha nacional "
            "*atual* em fase 3+ neste extrato. É uma lacuna de cobertura, "
            "não prova de que não há fome."
        ),
        methods_md=_METHODS["pt"],
        sources_md=_SOURCES["pt"],
        ethics_md=_ETHICS["pt"],
    ),
    "es": _pack(
        lang_label="Idioma",
        sidebar_hint="Cambie de idioma en cualquier momento. Toda la página se actualiza.",
        sidebar_guide="Empiece por **Historia**, es la conclusión principal. Mapa y País son acercamientos opcionales.",
        reset_view="Volver a Historia",
        status_ready="Tabla de análisis cargada",
        load_error="No se pudo abrir la tabla de análisis: {detail}. Vuelva a ejecutar `python -m src.run_pipeline` y luego actualice.",
        kpi_ipc_help="Personas en fase IPC 3+ (Crisis o peor) en los ocho países focales con una estimación nacional vigente.",
        kpi_disp_help="Refugiados + solicitantes de asilo + otras personas de interés acogidas en el país de asilo (ACNUR).",
        kpi_u5_help="Mediana de la OMS de mortalidad en menores de 5 años (muertes por 1.000 nacidos vivos) en el conjunto focal.",
        eyebrow="Portafolio de datos humanitarios",
        title="Donde las necesidades se superponen",
        why=(
            "El hambre, el desplazamiento y el riesgo para la supervivencia infantil rara vez aparecen solos. "
            "Este panel muestra dónde estas presiones se acumulan, para que las prioridades sigan a las "
            "personas, no a los compartimentos institucionales."
        ),
        def_expander="Cómo contamos el desplazamiento (lectura rápida)",
        def_title="Definición que fijamos",
        def_body=(
            "Personas **acogidas** en el país de asilo: refugiados + solicitantes de asilo + "
            "otras personas de interés (ACNUR). Dejamos fuera a propósito los recuentos por país de "
            "origen, mezclarlos hace que los gráficos parezcan más elegantes y las respuestas más confusas."
        ),
        kpi_ipc="En fase IPC 3+ (países focales)",
        kpi_disp="Personas desplazadas acogidas",
        kpi_u5="Mediana de mortalidad en menores de 5 años",
        nav_label="¿Dónde quiere mirar?",
        nav_story="Historia",
        nav_map="Mapa",
        nav_country="Un país",
        nav_about="Detrás de las cifras",
        insight_title="En palabras simples",
        action_heading="Qué mirar a continuación",
        action_dual_pressure=(
            "**{countries}** están en niveles altos tanto en severidad del hambre como en desplazamiento "
            "acogido, compare los planes de seguridad alimentaria y protección antes de decidir dónde actuar primero."
        ),
        action_missing_ipc=(
            "**{countries}**: no hay una estimación nacional vigente de IPC Fase 3+ en esta tabla, "
            "trate una celda vacía del mapa como desconocida, no como riesgo bajo."
        ),
        action_single_axis=(
            "Los países urgentes en una sola dimensión (vea el contraste arriba) igual merecen una "
            "mirada específica, no solo el conjunto de doble presión."
        ),
        country_select="Elija un país",
        trends_title="Cómo ha evolucionado la situación",
        trends_intro="El mismo país, con un poco más de contexto en el tiempo, desplazamiento acogido y mortalidad infantil.",
        footer="Un portafolio de aprendizaje para roles de datos humanitarios · No apto para decisiones operativas",
        demo_note="Vea el recorrido de 90 segundos",
        demo_watch="Abrir demo",
        access_dates="Datos extraídos el",
        access_dates_hint=",  las fuentes están en Detrás de las cifras",
        loading="Preparando la última tabla…, un momento.",
        no_data=(
            "Todavía no hay tabla de análisis, ejecute un pipeline limpio y luego actualice.\n\n"
            "Desde la carpeta del proyecto:\n\n```bash\npython -m src.run_pipeline\n```\n\nLuego actualice esta página."
        ),
        map_takeaway=(
            "Más oscuro = una proporción mayor de personas en fase IPC 3+ (Crisis o peor). "
            "Trate esto como un telón de fondo de severidad antes de pasar a la vista de Historia."
        ),
        trends_caption=(
            "Estas líneas provienen del historial de acogida de ACNUR y de la mortalidad en menores de 5 "
            "años de la OMS. Las evaluaciones IPC no llegan en un calendario mensual ordenado, así que no "
            "simulamos una tendencia de hambre uniforme."
        ),
        about_intro="Para quienes quieren ver el funcionamiento interno: métodos, glosario, fuentes y límites.",
        glossary_heading="### Palabras que usamos a propósito",
        access_date_label="Extraídos el",
        chart_map_title="Inseguridad alimentaria aguda (IPC Fase 3+) en países focales",
        chart_map_pct="IPC Fase 3+ (%)",
        chart_map_people="Personas en Fase 3+",
        chart_map_disp="Desplazados (acogidos)",
        chart_map_u5="Mortalidad en menores de 5 años",
        chart_map_colorbar="% en Fase 3+",
        chart_scatter_title="Dónde coinciden el desplazamiento y el hambre",
        chart_scatter_x="Personas desplazadas acogidas (ACNUR)",
        chart_scatter_y="Población en fase IPC 3+ (%)",
        chart_scatter_u5="Mortalidad en menores de 5 años (por 1000)",
        chart_drill_p1="Personas en fase IPC 3+",
        chart_drill_p2="Desplazados acogidos",
        chart_drill_p3="Mortalidad en menores de 5 años frente a la mediana focal",
        chart_drill_bar_ipc="Fase 3+",
        chart_drill_bar_disp="Desplazados",
        chart_drill_median="Mediana focal",
        chart_drill_title="{country} de un vistazo",
        chart_no_data="Todavía no hay nada para {iso3}",
        chart_trends_p1="Desplazamiento acogido (ACNUR)",
        chart_trends_p2="Mortalidad en menores de 5 años (OMS)",
        chart_trends_series_disp="Desplazados acogidos",
        chart_trends_series_u5="TMM5",
        chart_trends_title="{country} en los últimos años",
        country_gap=(
            "No encontramos una estimación nacional vigente de IPC Fase 3+ para {country} en este extracto. "
            "Eso no significa que no haya hambre, solo que este fragmento de datos públicos está en silencio. "
            "Lea el desplazamiento y la mortalidad infantil teniendo en cuenta este vacío."
        ),
        country_snapshot=(
            "En {country}, cerca del **{pct}%** de la población evaluada está en fase 3+, "
            "con **{displaced}** personas desplazadas acogidas y una mortalidad en menores de 5 años "
            "de alrededor de **{u5mr}** por 1.000 nacidos vivos."
        ),
        insight_headline=(
            "Mayor doble presión: {names} se sitúan en o por encima de las medianas del conjunto focal "
            "tanto en la proporción de IPC Fase 3+ ({ipc_pct}%) como en el desplazamiento acogido "
            "({displaced} personas)."
        ),
        insight_headline_empty="Ningún país se sitúa por encima de ambas medianas en el extracto actual.",
        insight_contrast=(
            " Nota: {country} tiene una Fase 3+ alta ({ipc_pct}%) pero un desplazamiento acogido más bajo, "
            "el hambre y la acogida de asilo son señales distintas."
        ),
        insight_gap=(
            " Vacío: {names} {verb} un registro nacional vigente de IPC Fase 3+ aquí, "
            "dato faltante, no necesidad nula."
        ),
        insight_body_lead=(
            "Para los equipos de programa: comiencen por el conjunto de doble presión, luego discutan "
            "juntos seguridad alimentaria y protección."
        ),
        map_gap_note=(
            "**La ausencia de IPC en el mapa es intencional.** {names} {verb} un registro nacional "
            "*vigente* en fase 3+ en este extracto. Eso es un vacío de cobertura, no una prueba de que "
            "el hambre esté ausente."
        ),
        methods_md=_METHODS["es"],
        sources_md=_SOURCES["es"],
        ethics_md=_ETHICS["es"],
    ),
    "ar": _pack(
        lang_label="اللغة",
        sidebar_hint="يمكنك تغيير اللغة في أي وقت، وستتحدث الصفحة بأكملها تبعاً لذلك.",
        sidebar_guide="ابدأ بقسم **القصة**، فهو الخلاصة الرئيسية. الخريطة والدولة تكبيران اختياريان.",
        reset_view="العودة إلى القصة",
        status_ready="تم تحميل جدول التحليل",
        load_error="تعذر فتح جدول التحليل: {detail}. أعد تشغيل `python -m src.run_pipeline` ثم حدّث الصفحة.",
        kpi_ipc_help="الأشخاص في المرحلة 3 فأعلى من التصنيف المرحلي المتكامل للأمن الغذائي (IPC)، أزمة أو أسوأ، في الدول الثماني المستهدفة ممن لديهم تقدير وطني حالي.",
        kpi_disp_help="اللاجئون وطالبو اللجوء وسائر الأشخاص موضع الاهتمام المستضافون في بلد اللجوء (المفوضية السامية لشؤون اللاجئين).",
        kpi_u5_help="وسيط منظمة الصحة العالمية لمعدل وفيات الأطفال دون سن الخامسة (لكل 1000 ولادة حية) في المجموعة المستهدفة.",
        eyebrow="حافظة بيانات إنسانية",
        title="حيث تتقاطع الاحتياجات",
        why=(
            "نادراً ما يظهر الجوع والنزوح ومخاطر بقاء الأطفال منفردين. "
            "تُظهر هذه اللوحة أين تتراكم هذه الضغوط، لتتبع الأولويات الأشخاص لا القطاعات المنعزلة."
        ),
        def_expander="كيف نحتسب النزوح (قراءة سريعة)",
        def_title="التعريف الذي اعتمدناه",
        def_body=(
            "الأشخاص **المستضافون** في بلد اللجوء: اللاجئون + طالبو اللجوء + الأشخاص الآخرون موضع "
            "الاهتمام (المفوضية). نستبعد عمداً الأعداد المصنّفة حسب بلد المنشأ، فخلطها يجعل الرسوم "
            "البيانية تبدو أذكى والإجابات أكثر ضبابية."
        ),
        kpi_ipc="في المرحلة 3 فأعلى من IPC (الدول المستهدفة)",
        kpi_disp="النازحون المستضافون",
        kpi_u5="وسيط وفيات الأطفال دون الخامسة",
        nav_label="أين تريد أن تنظر؟",
        nav_story="القصة",
        nav_map="الخريطة",
        nav_country="دولة واحدة",
        nav_about="خلف الأرقام",
        insight_title="بعبارات بسيطة",
        action_heading="ما الذي يستحق النظر إليه لاحقاً",
        action_dual_pressure=(
            "تحتل **{countries}** مرتبة عالية في كل من شدة الجوع والنزوح المستضاف، "
            "فقارن خطط الأمن الغذائي والحماية قبل تحديد أولوية العمل."
        ),
        action_missing_ipc=(
            "**{countries}**: لا يوجد تقدير وطني حالي لمرحلة IPC 3 فأعلى في هذا الجدول، "
            "وينبغي التعامل مع خانة الخريطة الفارغة على أنها غير معروفة لا منخفضة الخطورة."
        ),
        action_single_axis=(
            "الدول الملحة على بُعد واحد فقط (انظر التباين أعلاه) ما تزال تستحق نظرة مخصصة، "
            "لا مجموعة الضغط المزدوج وحدها."
        ),
        country_select="اختر دولة",
        trends_title="كيف تطورت الأوضاع",
        trends_intro="الدولة نفسها، مع سياق زمني أطول قليلاً، للنزوح المستضاف ووفيات الأطفال.",
        footer="حافظة تعلّم لأدوار بيانات العمل الإنساني · غير مخصصة لاتخاذ قرارات تشغيلية",
        demo_note="شاهد الجولة التوضيحية التي تستغرق 90 ثانية",
        demo_watch="فتح العرض التوضيحي",
        access_dates="تاريخ سحب البيانات",
        access_dates_hint="،  والمصادر متاحة ضمن خلف الأرقام",
        loading="جارٍ تجميع أحدث جدول… لحظات من فضلك.",
        no_data=(
            "لا يوجد جدول تحليل بعد، شغّل خط معالجة نظيفاً ثم حدّث الصفحة.\n\n"
            "من داخل مجلد المشروع:\n\n```bash\npython -m src.run_pipeline\n```\n\nثم حدّث هذه الصفحة."
        ),
        map_takeaway=(
            "كلما ازداد التدرج اللوني غموقاً، ارتفعت نسبة السكان في المرحلة 3 فأعلى من IPC "
            "(أزمة أو أسوأ). اعتبر هذه الخريطة خلفية لشدة الوضع قبل الانتقال إلى عرض القصة."
        ),
        trends_caption=(
            "تأتي هذه الخطوط من سجل استضافة المفوضية ومعدل وفيات الأطفال دون الخامسة لمنظمة الصحة "
            "العالمية. تقييمات IPC لا تصدر وفق تقويم شهري منتظم، لذلك لا نصطنع اتجاهاً سلساً للجوع."
        ),
        about_intro="لمن يرغب في الاطلاع على التفاصيل: المنهجية والمسرد والمصادر والحدود.",
        glossary_heading="### مصطلحات اخترناها عمداً",
        access_date_label="تاريخ السحب",
        chart_map_title="انعدام الأمن الغذائي الحاد (IPC المرحلة 3 فأعلى) في الدول المستهدفة",
        chart_map_pct="IPC المرحلة 3 فأعلى (%)",
        chart_map_people="الأشخاص في المرحلة 3 فأعلى",
        chart_map_disp="النازحون (المستضافون)",
        chart_map_u5="وفيات الأطفال دون الخامسة",
        chart_map_colorbar="% في المرحلة 3 فأعلى",
        chart_scatter_title="أين يلتقي النزوح بالجوع",
        chart_scatter_x="النازحون المستضافون (المفوضية)",
        chart_scatter_y="السكان في مرحلة IPC 3 فأعلى (%)",
        chart_scatter_u5="وفيات الأطفال دون الخامسة (لكل 1000)",
        chart_drill_p1="الأشخاص في مرحلة IPC 3 فأعلى",
        chart_drill_p2="النازحون المستضافون",
        chart_drill_p3="وفيات الأطفال دون الخامسة مقابل الوسيط المستهدف",
        chart_drill_bar_ipc="المرحلة 3 فأعلى",
        chart_drill_bar_disp="النازحون",
        chart_drill_median="الوسيط المستهدف",
        chart_drill_title="{country} في لمحة",
        chart_no_data="لا توجد بيانات بعد لـ {iso3}",
        chart_trends_p1="النزوح المستضاف (المفوضية)",
        chart_trends_p2="وفيات الأطفال دون الخامسة (منظمة الصحة العالمية)",
        chart_trends_series_disp="النازحون المستضافون",
        chart_trends_series_u5="معدل وفيات الأطفال دون الخامسة",
        chart_trends_title="{country} خلال السنوات الأخيرة",
        country_gap=(
            "لم نعثر على تقدير وطني حالي لمرحلة IPC 3 فأعلى لدولة {country} في هذا المقتطف. "
            "هذا لا يعني غياب الجوع، بل يعني فقط أن هذا الجزء من البيانات العلنية صامت. اقرأ بيانات "
            "النزوح ووفيات الأطفال مع أخذ هذه الفجوة في الحسبان."
        ),
        country_snapshot=(
            "في {country}، نحو **{pct}%** من السكان الذين جرى تقييمهم يقعون في المرحلة 3 فأعلى، "
            "مع **{displaced}** من النازحين المستضافين، ومعدل وفيات للأطفال دون الخامسة يقارب "
            "**{u5mr}** لكل 1000 ولادة حية."
        ),
        insight_headline=(
            "أعلى ضغط مزدوج: تقف {names} عند وسيط المجموعة المستهدفة أو فوقه في كل من حصة مرحلة "
            "IPC 3 فأعلى ({ipc_pct}%) والنزوح المستضاف ({displaced} شخصاً)."
        ),
        insight_headline_empty="لا توجد دولة تقف فوق الوسيطين معاً في المقتطف الحالي.",
        insight_contrast=(
            " ملاحظة: تسجل {country} مرحلة 3 فأعلى مرتفعة ({ipc_pct}%) لكن بنزوح مستضاف أقل، "
            "فالجوع واستضافة اللجوء إشارتان مختلفتان."
        ),
        insight_gap=(
            " فجوة: {verb} {names} تقديراً وطنياً حالياً لمرحلة IPC 3 فأعلى هنا، "
            "وهذه بيانات مفقودة لا احتياج معدوم."
        ),
        insight_body_lead=(
            "لفرق البرامج: ابدأوا بمجموعة الضغط المزدوج، ثم ناقشوا الأمن الغذائي والحماية معاً."
        ),
        map_gap_note=(
            "**غياب بيانات IPC عن الخريطة أمر مقصود.** {verb} {names} صفاً وطنياً *حالياً* لمرحلة "
            "3 فأعلى في هذا المقتطف. هذه فجوة تغطية لا دليل على غياب الجوع."
        ),
        methods_md=_METHODS["ar"],
        sources_md=_SOURCES["ar"],
        ethics_md=_ETHICS["ar"],
    ),
    "zh": _pack(
        lang_label="语言",
        sidebar_hint="可随时切换语言，整页内容会同步更新。",
        sidebar_guide="从 **Story** 开始，, 这是核心结论。地图与国家视图为可选深入。",
        reset_view="返回 Story",
        status_ready="分析表已加载",
        load_error="无法打开分析表：{detail}。请运行 `python -m src.run_pipeline` 后刷新。",
        kpi_ipc_help="八个重点国家中，具备当前国家估计的 IPC 第 3+ 阶段（危机或更差）人口。",
        kpi_disp_help="收容国内的难民 + 寻求庇护者 + 其他受关切者（UNHCR）。",
        kpi_u5_help="重点国家组 WHO 5 岁以下儿童死亡率中位数（每 1,000 活产）。",
        eyebrow="人道主义数据作品集",
        title="需求重叠之处",
        why=(
            "饥饿、流离失所与儿童生存风险很少单独出现。"
            "本仪表盘呈现这些压力叠加之处，, 让优先排序跟随人，而非部门孤岛。"
        ),
        def_expander="我们如何统计流离失所（速读）",
        def_title="锁定的定义",
        def_body=(
            "在庇护国**收容**的人口：难民 + 寻求庇护者 + UNHCR 其他受关切者。"
            "故意不混用来源国口径，, 混用会使图表好看、结论模糊。"
        ),
        kpi_ipc="IPC 第 3+ 阶段（重点国家）",
        kpi_disp="收容的流离失所者",
        kpi_u5="5 岁以下死亡率中位数",
        nav_label="您想看哪里？",
        nav_story="Story",
        nav_map="地图",
        nav_country="一个国家",
        nav_about="数字背后",
        insight_title="直白说明",
        action_heading="接下来看什么",
        action_dual_pressure=(
            "**{countries}** 在饥饿严重程度和收容人数上都偏高，, "
            "在决定优先行动地点之前，先对照粮食安全与保护方面的计划。"
        ),
        action_missing_ipc=(
            "**{countries}** 在本表中没有当前全国 IPC 3 级及以上估计，, "
            "地图上的空白格表示未知，不代表低风险。"
        ),
        action_single_axis=(
            "只在单一维度上突出的国家（见上文对比）仍值得单独关注，, "
            "不应只看双重压力国家。"
        ),
        country_select="选择国家",
        trends_title="近期变化",
        trends_intro="同一国家，多一点时间背景，, 收容与儿童死亡率。",
        footer="人道主义数据岗位学习作品集 · 不用于业务决策",
        demo_note="90 秒演示",
        demo_watch="打开演示",
        access_dates="数据获取日期",
        access_dates_hint=",  来源见「数字背后」",
        loading="正在加载分析表…",
        no_data=(
            "尚无分析表，, 先跑通一次流水线，再刷新。\n\n"
            "在项目目录：\n\n```bash\npython -m src.run_pipeline\n```\n\n然后刷新本页。"
        ),
        map_takeaway=(
            "颜色越深 = IPC 第 3+ 阶段人口占比越高（危机或更差）。"
            "把它当作严重程度底图，再回到 Story。"
        ),
        trends_caption=(
            "曲线来自 UNHCR 收容历史与 WHO 5 岁以下死亡率。"
            "IPC 评估并非按月平滑出现，, 我们不伪造饥饿趋势线。"
        ),
        about_intro="适合想看方法细节的人，, 方法论、词汇表、来源与边界。",
        glossary_heading="### 特意选用的术语",
        access_date_label="获取于",
        chart_map_title="急性粮食不安全（IPC 第 3+ 阶段）,  重点国家",
        chart_map_pct="IPC 第 3+ 阶段（%）",
        chart_map_people="第 3+ 阶段人口",
        chart_map_disp="流离失所者（收容）",
        chart_map_u5="5 岁以下死亡率",
        chart_map_colorbar="第 3+ 阶段 %",
        chart_scatter_title="流离失所与饥饿的交汇",
        chart_scatter_x="收容的流离失所者（UNHCR）",
        chart_scatter_y="IPC 第 3+ 阶段人口占比（%）",
        chart_scatter_u5="5 岁以下死亡率（每 1000）",
        chart_drill_p1="IPC 第 3+ 阶段人口",
        chart_drill_p2="收容的流离失所者",
        chart_drill_p3="5 岁以下死亡率 vs 组中位数",
        chart_drill_bar_ipc="第 3+ 阶段",
        chart_drill_bar_disp="流离失所者",
        chart_drill_median="组中位数",
        chart_drill_title="{country} 一览",
        chart_no_data="暂无 {iso3} 的数据",
        chart_trends_p1="收容（UNHCR）",
        chart_trends_p2="5 岁以下死亡率（WHO）",
        chart_trends_series_disp="收容的流离失所者",
        chart_trends_series_u5="U5MR",
        chart_trends_title="{country} 近年趋势",
        country_gap=(
            "本摘录中找不到 {country} 当前国家层面 IPC 第 3+ 阶段估计。"
            "这不表示「没有饥饿」, , 只表示这块公开数据暂时空白。"
        ),
        country_snapshot=(
            "在 {country}，约 **{pct}%** 被评估人口处于第 3+ 阶段，"
            "收容流离失所者 **{displaced}** 人，5 岁以下死亡率约 "
            "**{u5mr}**/1,000 活产。"
        ),
        insight_headline=(
            "双重压力最高：{names} 同时处于或高于重点组中位数，, "
            "IPC 第 3+ 阶段占比（{ipc_pct}%）与收容流离失所者（{displaced} 人）。"
        ),
        insight_headline_empty="本摘录中没有国家同时高于两项中位数。",
        insight_contrast=(
            " 说明：{country} 第 3+ 阶段很高（{ipc_pct}%），但收容较低，, "
            "饥饿与收容是不同信号。"
        ),
        insight_gap=(
            " 缺口：{names}{verb}此处没有当前国家 IPC 第 3+ 阶段行，, "
            "数据缺失，不是零需求。"
        ),
        insight_body_lead=(
            "对项目团队：先从双重压力国家开始，再一起讨论粮食安全与保护。"
        ),
        map_gap_note=(
            "**地图上缺失 IPC 是有意为之。** {names}{verb}本摘录中没有*当前*国家第 3+ 阶段行。"
            "这是覆盖缺口，, 不能证明没有饥饿。"
        ),
        methods_md=_METHODS["zh"],
        sources_md=_SOURCES["zh"],
        ethics_md=_ETHICS["zh"],
    ),
    "ru": _pack(
        lang_label="Язык",
        sidebar_hint="Меняйте язык в любой момент, вся страница обновится.",
        sidebar_guide="Начните с **Story**, это главный вывод. Карта и страна, дополнительные срезы.",
        reset_view="Вернуться к Story",
        status_ready="Аналитическая таблица загружена",
        load_error="Не удалось открыть таблицу: {detail}. Запустите `python -m src.run_pipeline` и обновите страницу.",
        kpi_ipc_help="Люди в фазе IPC 3+ (кризис или хуже) по восьми странам с текущей национальной оценкой.",
        kpi_disp_help="Беженцы + просители убежища + прочие лица на территории страны убежища (УВКБ).",
        kpi_u5_help="Медиана смертности детей до 5 лет по ВОЗ (на 1 000 живорождений) по панели.",
        eyebrow="Портфолио гуманитарных данных",
        title="Где потребности пересекаются",
        why=(
            "Голод, перемещение и риск для выживания детей редко приходят поодиночке. "
            "Эта панель показывает, где давления накладываются, чтобы приоритеты следовали за людьми, а не за силосами."
        ),
        def_expander="Как мы считаем перемещение (кратко)",
        def_title="Зафиксированное определение",
        def_body=(
            "Лица, **принятые** в стране убежища: беженцы + просители убежища + "
            "прочие лица, подпадающие под мандат УВКБ. Показатели по стране происхождения намеренно не смешиваем."
        ),
        kpi_ipc="В фазе IPC 3+ (страны фокуса)",
        kpi_disp="Принятые перемещённые лица",
        kpi_u5="Медиана смертности <5 лет",
        nav_label="Куда смотреть?",
        nav_story="Story",
        nav_map="Карта",
        nav_country="Одна страна",
        nav_about="За цифрами",
        insight_title="Простыми словами",
        action_heading="На что смотреть дальше",
        action_dual_pressure=(
            "**{countries}** высоки и по тяжести IPC, и по приёму, "
            "сопоставьте планы продовольственной безопасности и защиты перед приоритизацией."
        ),
        action_missing_ipc=(
            "**{countries}**: в этой таблице нет актуальной национальной оценки IPC фазы 3+, "
            "пустая ячейка на карте означает «неизвестно», а не низкий риск."
        ),
        action_single_axis=(
            "Страны, срочные только по одному измерению (см. контраст выше), "
            "всё равно заслуживают отдельного взгляда, не только группа двойного давления."
        ),
        country_select="Выберите страну",
        trends_title="Как менялась картина",
        trends_intro="Та же страна, чуть больше временного контекста, приём и детская смертность.",
        footer="Учебное портфолио для ролей гуманитарных данных · Не для операционных решений",
        demo_note="Обзор на 90 секунд",
        demo_watch="Открыть демо",
        access_dates="Данные получены",
        access_dates_hint=",  источники в разделе «За цифрами»",
        loading="Загрузка аналитической таблицы…",
        no_data=(
            "Аналитической таблицы ещё нет, выполните чистый pipeline, затем обновите.\n\n"
            "В папке проекта:\n\n```bash\npython -m src.run_pipeline\n```\n\nЗатем обновите страницу."
        ),
        map_takeaway=(
            "Темнее = выше доля населения в фазе IPC 3+ (кризис или хуже). "
            "Используйте как фон тяжести, прежде чем вернуться к Story."
        ),
        trends_caption=(
            "Кривые из истории приёма УВКБ и смертности детей до 5 лет по ВОЗ. "
            "Оценки IPC не приходят ежемесячно, мы не рисуем ложный гладкий тренд голода."
        ),
        about_intro="Для тех, кто хочет заглянуть под капот, методы, глоссарий, источники и пределы.",
        glossary_heading="### Сознательно выбранные термины",
        access_date_label="Получено",
        chart_map_title="Острая продовольственная нестабильность (фаза IPC 3+), страны фокуса",
        chart_map_pct="Фаза IPC 3+ (%)",
        chart_map_people="Люди в фазе 3+",
        chart_map_disp="Перемещённые (принято)",
        chart_map_u5="Смертность <5",
        chart_map_colorbar="% в фазе 3+",
        chart_scatter_title="Где пересекаются перемещение и голод",
        chart_scatter_x="Принятые перемещённые лица (УВКБ)",
        chart_scatter_y="Население в фазе IPC 3+ (%)",
        chart_scatter_u5="Смертность <5 (на 1000)",
        chart_drill_p1="Люди в фазе IPC 3+",
        chart_drill_p2="Принятые перемещённые",
        chart_drill_p3="Смертность <5 vs медиана панели",
        chart_drill_bar_ipc="Фаза 3+",
        chart_drill_bar_disp="Перемещённые",
        chart_drill_median="Медиана панели",
        chart_drill_title="{country} кратко",
        chart_no_data="Пока нет данных для {iso3}",
        chart_trends_p1="Приём (УВКБ)",
        chart_trends_p2="Смертность <5 (ВОЗ)",
        chart_trends_series_disp="Принятые перемещённые",
        chart_trends_series_u5="U5MR",
        chart_trends_title="{country} за последние годы",
        country_gap=(
            "В этой выгрузке нет текущей национальной оценки фазы IPC 3+ для {country}. "
            "Это не «нет голода», лишь то, что этот срез публичных данных молчит."
        ),
        country_snapshot=(
            "В {country} около **{pct}%** оценённого населения в фазе 3+, "
            "при **{displaced}** принятых перемещённых лицах и смертности детей до 5 лет "
            "около **{u5mr}** на 1 000 живорождений."
        ),
        insight_headline=(
            "Наибольшее двойное давление: {names} на уровне или выше медиан панели "
            "по доле фазы IPC 3+ ({ipc_pct}%) и принятым перемещённым ({displaced} человек)."
        ),
        insight_headline_empty="В этой выгрузке ни одна страна не выше обеих медиан.",
        insight_contrast=(
            " Заметка: у {country} высокая фаза 3+ ({ipc_pct}%), но меньший приём, "
            "голод и приём, разные сигналы."
        ),
        insight_gap=(
            " Пробел: у {names} {verb} текущей строки IPC фазы 3+ здесь, "
            "нет данных, не нулевая потребность."
        ),
        insight_body_lead=(
            "Для программных команд: начните с группы двойного давления, "
            "затем обсудите продовольственную безопасность и защиту вместе."
        ),
        map_gap_note=(
            "**Отсутствие IPC на карте намеренно.** У {names} {verb} *текущей* национальной "
            "строки фазы 3+ в этой выгрузке. Это пробел покрытия, не доказательство отсутствия голода."
        ),
        methods_md=_METHODS["ru"],
        sources_md=_SOURCES["ru"],
        ethics_md=_ETHICS["ru"],
    ),
}

GLOSSARY = {
    "de": [
        ("IPC-Phase 3+", "Integrated Food Security Phase Classification. Krise oder schlimmer."),
        ("Aufnahmeland", "Country of asylum. Personen, die in diesem Land aufgenommen werden."),
        ("Herkunftsland", "Country of origin, hier nicht verwendet."),
        ("PoC", "Persons of concern (UNHCR); wir nutzen REF+ASY+OOC."),
        ("U5MR", "Sterblichkeit unter fünf Jahren (pro 1.000 Lebendgeburten), WHO GHO."),
        ("ISO3", "Dreistellige Ländercodes für sichere Joins."),
    ],
    "it": [
        ("IPC fase 3+", "Integrated Food Security Phase Classification. Crisi o peggio."),
        ("Paese di asilo", "Persone ospitate in quel paese."),
        ("Paese di origine", "Da dove le persone sono fuggite (non usato qui)."),
        ("PoC", "Persons of concern UNHCR (usiamo REF+ASY+OOC)."),
        ("U5MR", "Mortalità sotto i cinque anni (per 1.000 nati vivi), WHO GHO."),
        ("ISO3", "Codici paese a tre lettere per i join."),
    ],
    "pt": [
        ("IPC fase 3+", "Integrated Food Security Phase Classification. Crise ou pior."),
        ("País de asilo", "Pessoas acolhidas nesse país."),
        ("País de origem", "De onde as pessoas fugiram (não usado aqui)."),
        ("PoC", "Persons of concern ACNUR (usamos REF+ASY+OOC)."),
        ("U5MR", "Mortalidade em menores de cinco anos (por 1.000 nados-vivos), OMS GHO."),
        ("ISO3", "Códigos de país de três letras para junções."),
    ],
    "es": [
        ("IPC Fase 3+", "Clasificación Integrada de Fases de Seguridad Alimentaria. Crisis o peor."),
        ("País de asilo / acogida", "Personas acogidas en ese país (enfoque usado aquí)."),
        ("País de origen", "De dónde huyeron las personas desplazadas (no se usa aquí)."),
        ("PoC", "Personas de interés para ACNUR (categoría más amplia; aquí usamos REF+ASY+OOC)."),
        ("TMM5", "Tasa de mortalidad en menores de 5 años (muertes por 1.000 nacidos vivos), OMS GHO."),
        ("ISO3", "Códigos de país de tres letras usados para unir todas las fuentes de forma segura."),
    ],
    "ar": [
        ("مرحلة IPC 3 فأعلى", "التصنيف المرحلي المتكامل للأمن الغذائي. أزمة أو أسوأ."),
        ("بلد اللجوء / الاستضافة", "الأشخاص المستضافون في ذلك البلد (النهج المعتمد هنا)."),
        ("بلد المنشأ", "البلد الذي فرّ منه الأشخاص النازحون (غير مستخدم هنا)."),
        ("الأشخاص موضع الاهتمام (PoC)", "الأشخاص الذين تُعنى بهم المفوضية (فئة أوسع؛ نستخدم هنا اللاجئين وطالبي اللجوء وسائر الأشخاص موضع الاهتمام)."),
        ("معدل وفيات الأطفال دون الخامسة", "عدد الوفيات لكل 1000 ولادة حية، منظمة الصحة العالمية GHO."),
        ("ISO3", "رموز الدول المكوّنة من ثلاثة أحرف، تُستخدم لربط جميع المصادر بأمان."),
    ],
    "zh": [
        ("IPC 第 3+ 阶段", "综合粮食安全阶段分类, 危机或更差。"),
        ("庇护国 / 收容", "在该国被收容的人口。"),
        ("来源国", "逃离来源国（此处不用）。"),
        ("PoC", "UNHCR 受关切者（我们使用 REF+ASY+OOC）。"),
        ("U5MR", "五岁以下儿童死亡率（每 1,000 活产），WHO GHO。"),
        ("ISO3", "用于安全关联的三位国家代码。"),
    ],
    "ru": [
        ("Фаза IPC 3+", "Интегрированная классификация продовольственной безопасности, кризис или хуже."),
        ("Страна убежища", "Лица, принятые на территории этой страны."),
        ("Страна происхождения", "Откуда бежали (здесь не используется)."),
        ("PoC", "Persons of concern УВКБ (мы используем REF+ASY+OOC)."),
        ("U5MR", "Смертность детей до пяти лет (на 1 000 живорождений), ВОЗ GHO."),
        ("ISO3", "Трёхбуквенные коды стран для соединений."),
    ],
}

# Verb forms for gap notes: (singular, plural)
GAP_VERBS = {
    "de": ("hat", "haben"),
    "it": ("non ha", "non hanno"),
    "pt": ("não tem", "não têm"),
    "es": ("no tiene", "no tienen"),
    # Arabic uses the invariant "لا يوجد لدى" (there isn't, with X) construction so the
    # verb doesn't need to agree in gender/number with the list of country names.
    "ar": ("لا يوجد لدى", "لا يوجد لدى"),
    "zh": ("在", "在"),  # Chinese templates embed grammar differently; see insights
    "ru": ("нет", "нет"),
}
