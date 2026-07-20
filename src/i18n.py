"""
Multilingual UI copy (EN/FR/DE/IT/PT/ZH/RU).

Every user-visible string should live here or in src.locales_extra.
"""

from __future__ import annotations

from src.config import FOCUS_NAMES
from src import locales_extra

FOCUS_NAMES_I18N = {
    "en": FOCUS_NAMES,
    "fr": {
        "BFA": "Burkina Faso",
        "TCD": "Tchad",
        "ETH": "Éthiopie",
        "MLI": "Mali",
        "NER": "Niger",
        "SOM": "Somalie",
        "SSD": "Soudan du Sud",
        "SDN": "Soudan",
    },
    **locales_extra.FOCUS_NAMES,
}

LANGUAGE_OPTIONS: tuple[str, ...] = ("en", "fr", "de", "it", "pt", "zh", "ru")

LANGUAGE_LABELS: dict[str, str] = {
    "en": "English",
    "fr": "Français",
    "de": "Deutsch",
    "it": "Italiano",
    "pt": "Português",
    "zh": "中文",
    "ru": "Русский",
}

COPY = {
    "en": {
        "lang_label": "Language",
        "sidebar_hint": "Switch language anytime. Everything on the page follows.",
        "sidebar_guide": "Start on **Story**, that’s the main takeaway. Map and Country are optional zoom-ins.",
        "reset_view": "Back to Story",
        "status_ready": "Analysis table loaded",
        "load_error": "Could not open the analysis table: {detail}. Re-run `python -m src.run_pipeline`, then refresh.",
        "kpi_ipc_help": "People in IPC Phase 3+ (Crisis or worse) across the eight focus countries with a current national estimate.",
        "kpi_disp_help": "Refugees + asylum-seekers + others of concern hosted in country of asylum (UNHCR).",
        "kpi_u5_help": "Median WHO under-5 mortality (deaths per 1,000 live births) across the focus set.",
        "eyebrow": "Humanitarian data portfolio",
        "title": "Where Needs Overlap",
        "why": (
            "Hunger, displacement, and child survival risk rarely show up alone. "
            "This dashboard surfaces where those pressures compound, so priorities follow people, not silos."
        ),
        "def_expander": "How we count displacement (quick read)",
        "def_title": "Definition we locked in",
        "def_body": (
            "People **hosted** in the country of asylum: refugees + asylum-seekers + "
            "others of concern (UNHCR). We leave origin-based counts out on purpose, "
            "mixing them makes charts look clever and answers fuzzy."
        ),
        "kpi_ipc": "In IPC Phase 3+ (focus countries)",
        "kpi_disp": "Displaced people hosted",
        "kpi_u5": "Median under-5 mortality",
        "nav_label": "Where do you want to look?",
        "nav_story": "Story",
        "nav_map": "Map",
        "nav_country": "One country",
        "nav_about": "Behind the numbers",
        "insight_title": "In plain words",
        "action_heading": "What to look at next",
        "action_dual_pressure": (
            "**{countries}** rank high on both hunger severity and hosted displacement, "
            "compare food-security and protection plans before you pick where to act first."
        ),
        "action_missing_ipc": (
            "**{countries}**: no current national IPC Phase 3+ estimate in this table, "
            "treat a blank map cell as unknown, not low risk."
        ),
        "action_single_axis": (
            "Countries urgent on only one dimension (see the contrast above) still deserve "
            "a targeted look, not only the dual-pressure set."
        ),
        "country_select": "Choose a country",
        "trends_title": "How things have been moving",
        "trends_intro": "Same country, a little more time context, hosted displacement and child mortality.",
        "footer": "A learning portfolio for humanitarian data roles · Not for operational decisions",
        "demo_note": "Watch the 90-second walkthrough",
        "demo_watch": "Open demo",
        "access_dates": "Data pulled on",
        "access_dates_hint": ",  sources live under Behind the numbers",
        "loading": "Pulling the latest table together… hang tight.",
        "no_data": (
            "No analysis table yet, run one clean pipeline, then refresh.\n\n"
            "From the project folder:\n\n"
            "```bash\n"
            "python -m src.run_pipeline\n"
            "```\n\n"
            "Then refresh this page."
        ),
        "map_takeaway": (
            "Darker = a larger share of people in IPC Phase 3+ (Crisis or worse). "
            "Treat this as a severity backdrop before you lean into the Story view."
        ),
        "trends_caption": (
            "These lines come from UNHCR hosting history and WHO under-5 mortality. "
            "IPC assessments don’t arrive on a neat monthly calendar, so we don’t fake a smooth hunger trend."
        ),
        "about_intro": "For people who want to peek under the hood, methods, glossary, sources, and limits.",
        "glossary_heading": "### Words we use on purpose",
        "methods_md": """### How the numbers are built
- **Join key:** ISO3 codes (we never join on English country names).
- **IPC:** HDX long file → keep `Validity period == current` and `Phase == 3+`. Shares arrive as 0–1 and become percents for charts.
- **Displacement:** UNHCR API with `coa` + `cf_type=ISO`. We add refugees + asylum-seekers + others of concern **hosted** in-country. Omitting `coa` returns a world aggregate, a common API failure mode.
- **Child survival:** WHO GHO `MDG_0000000001`, latest year per focus country.
- **Compound score:** an illustrative z-score blend for conversation only, not an official index.

More detail lives in `docs/methods.md`.
""",
        "sources_md": """### Where the data comes from
- **IPC acute food insecurity** on [HDX](https://data.humdata.org/dataset/global-acute-food-insecurity-country-data)
- **UNHCR Population Statistics API**, hosted refugees, asylum-seekers, others of concern
- **WHO GHO**, under-5 mortality (`MDG_0000000001`)
""",
        "access_date_label": "Pulled on",
        "ethics_md": """### Care & limits
- Public aggregates only, no attempt to identify communities or individuals
- Country totals hide hotspots; do not target aid from this page alone
- This is a **portfolio learning project**, not an OCHA / UNICEF / UNHCR product

Longer honesty sheet: `docs/limitations.md`.
""",
        "chart_map_title": "Acute food insecurity (IPC Phase 3+) in focus countries",
        "chart_map_pct": "IPC Phase 3+ (%)",
        "chart_map_people": "People in Phase 3+",
        "chart_map_disp": "Displaced (hosted)",
        "chart_map_u5": "Under-5 mortality",
        "chart_map_colorbar": "% in Phase 3+",
        "chart_scatter_title": "Where displacement and hunger sit together",
        "chart_scatter_x": "Displaced people hosted (UNHCR)",
        "chart_scatter_y": "Population in IPC Phase 3+ (%)",
        "chart_scatter_u5": "Under-5 mortality (per 1000)",
        "chart_drill_p1": "People in IPC Phase 3+",
        "chart_drill_p2": "Displaced hosted",
        "chart_drill_p3": "Under-5 mortality vs focus median",
        "chart_drill_bar_ipc": "Phase 3+",
        "chart_drill_bar_disp": "Displaced",
        "chart_drill_median": "Focus median",
        "chart_drill_title": "{country} at a glance",
        "chart_no_data": "Nothing here yet for {iso3}",
        "chart_trends_p1": "Hosted displacement (UNHCR)",
        "chart_trends_p2": "Under-5 mortality (WHO)",
        "chart_trends_series_disp": "Displaced hosted",
        "chart_trends_series_u5": "U5MR",
        "chart_trends_title": "{country} over recent years",
        "country_gap": (
            "We couldn’t find a current national IPC Phase 3+ estimate for {country} in this extract. "
            "That doesn’t mean there’s no hunger, only that this slice of public data is quiet. "
            "Read displacement and child mortality with that gap in mind."
        ),
        "country_snapshot": (
            "In {country}, about **{pct}%** of the assessed population is in Phase 3+, "
            "with **{displaced}** displaced people hosted and under-5 mortality around "
            "**{u5mr}** per 1,000 live births."
        ),
        "insight_headline": (
            "Highest dual pressure: {names} sit at or above the focus-set medians "
            "for both IPC Phase 3+ share ({ipc_pct}%) and hosted displacement "
            "({displaced} people)."
        ),
        "insight_headline_empty": "No country sits above both medians in the current extract.",
        "insight_contrast": (
            " Note: {country} has high Phase 3+ ({ipc_pct}%) but lower hosted displacement, "
            "hunger and asylum hosting are different signals."
        ),
        "insight_gap": (
            " Gap: {names} {verb} no current national IPC Phase 3+ row here, "
            "missing data, not zero need."
        ),
        "insight_body_lead": (
            "For programme teams: begin with the dual-pressure set, then discuss "
            "food security and protection together."
        ),
        "map_gap_note": (
            "**Missing IPC on the map is intentional.** {names} {verb} no *current* national "
            "Phase 3+ row in this extract. That is a coverage gap, not proof hunger is absent."
        ),
        "gap_verb_singular": "has",
        "gap_verb_plural": "have",
    },
    "fr": {
        "lang_label": "Langue",
        "sidebar_hint": "Changez de langue quand vous voulez. Toute la page suit.",
        "sidebar_guide": "Commencez par **Récit**, c’est l’essentiel. Carte et Pays sont des zooms optionnels.",
        "reset_view": "Retour au Récit",
        "status_ready": "Table d’analyse chargée",
        "load_error": "Impossible d’ouvrir la table d’analyse : {detail}. Relancez `python -m src.run_pipeline`, puis actualisez.",
        "kpi_ipc_help": "Personnes en phase IPC 3+ (Crise ou pire) dans les huit pays cibles avec une estimation nationale courante.",
        "kpi_disp_help": "Réfugiés + demandeurs d’asile + autres personnes accueillies dans le pays d’asile (HCR).",
        "kpi_u5_help": "Médiane OMS de la mortalité des moins de 5 ans (pour 1 000 naissances) sur le panel.",
        "eyebrow": "Portfolio de données humanitaires",
        "title": "Là où les besoins se croisent",
        "why": (
            "La faim, le déplacement et le risque pour la survie de l’enfant arrivent rarement seuls. "
            "Ce tableau de bord aide à voir où ils s’accumulent, pour que les priorités suivent "
            "les personnes, pas les silos."
        ),
        "def_expander": "Comment nous comptons le déplacement (lecture rapide)",
        "def_title": "Définition que nous avons figée",
        "def_body": (
            "Personnes **accueillies** dans le pays d’asile : réfugiés + demandeurs d’asile + "
            "autres personnes relevant du HCR. Nous laissons de côté les chiffres par origine, "
            "les mélanger rend les graphiques élégants et les réponses floues."
        ),
        "kpi_ipc": "En phase IPC 3+ (pays cibles)",
        "kpi_disp": "Personnes déplacées accueillies",
        "kpi_u5": "Mortalité <5 ans (médiane)",
        "nav_label": "Où voulez-vous regarder ?",
        "nav_story": "Récit",
        "nav_map": "Carte",
        "nav_country": "Un pays",
        "nav_about": "Derrière les chiffres",
        "insight_title": "En clair",
        "action_heading": "À regarder ensuite",
        "action_dual_pressure": (
            "**{countries}** sont élevés à la fois sur la sévérité IPC et l’accueil, "
            "comparez les plans sécurité alimentaire et protection avant de prioriser."
        ),
        "action_missing_ipc": (
            "**{countries}** : pas d’estimation nationale IPC Phase 3+ actuelle dans ce tableau, "
            "une case vide sur la carte signifie inconnu, pas faible risque."
        ),
        "action_single_axis": (
            "Un pays peut être urgent sur une seule dimension (voir le contraste ci-dessus), "
            "il mérite encore un regard ciblé, pas seulement l’ensemble à double pression."
        ),
        "country_select": "Choisir un pays",
        "trends_title": "Comment les choses ont bougé",
        "trends_intro": "Même pays, un peu plus de contexte dans le temps, accueil et mortalité infantile.",
        "footer": "Portfolio d’apprentissage pour métiers data humanitaires · Pas pour des décisions opérationnelles",
        "demo_note": "Voir la visite guidée (90 sec)",
        "demo_watch": "Ouvrir la démo",
        "access_dates": "Données extraites le",
        "access_dates_hint": ",  sources sous Derrière les chiffres",
        "loading": "On assemble la table d’analyse… encore un instant.",
        "no_data": (
            "Pas encore de table d’analyse, lancez un passage propre, puis actualisez.\n\n"
            "Depuis le dossier du projet :\n\n"
            "```bash\n"
            "python -m src.run_pipeline\n"
            "```\n\n"
            "Puis actualisez cette page."
        ),
        "map_takeaway": (
            "Plus foncé = part plus élevée de population en phase IPC 3+ (Crise ou pire). "
            "Gardez cette couche comme toile de fond avant de revenir au Récit."
        ),
        "trends_caption": (
            "Ces courbes viennent de l’historique d’accueil HCR et de la mortalité <5 ans OMS. "
            "Les évaluations IPC n’arrivent pas chaque mois comme une horloge, "
            "nous n’inventons pas une tendance lisse."
        ),
        "about_intro": "Pour celles et ceux qui veulent regarder sous le capot, méthodes, glossaire, sources et limites.",
        "glossary_heading": "### Des mots choisis exprès",
        "methods_md": """### Comment les chiffres sont construits
- **Clé de jointure :** codes ISO3 (jamais les noms de pays en toutes lettres).
- **IPC :** fichier long HDX → garder `Validity period == current` et `Phase == 3+`. Les parts arrivent en 0–1, puis deviennent des pourcentages.
- **Déplacement :** API HCR avec `coa` + `cf_type=ISO`. Nous additionnons réfugiés + demandeurs d’asile + autres personnes **accueillies**. Sans `coa`, on télécharge par accident le total mondial, piège classique.
- **Survie de l’enfant :** OMS GHO `MDG_0000000001`, dernière année par pays cible.
- **Score composé :** mélange illustratif de z-scores pour la conversation, pas un indice officiel.

Plus de détail dans `docs/methods.md`.
""",
        "sources_md": """### D’où viennent les données
- **IPC, insécurité alimentaire aiguë** sur [HDX](https://data.humdata.org/dataset/global-acute-food-insecurity-country-data)
- **API statistiques de population HCR**, réfugiés, demandeurs d’asile, autres personnes accueillies
- **OMS GHO**, mortalité des moins de 5 ans (`MDG_0000000001`)
""",
        "access_date_label": "Extraites le",
        "ethics_md": """### Soin & limites
- Agrégats publics seulement, aucune tentative d’identifier des communautés ou individus
- Les totaux nationaux masquent les hotspots, ne ciblez pas l’aide avec cette seule page
- **Projet de portfolio pédagogique**, pas un produit OCHA / UNICEF / HCR

Plus d’honnêteté dans `docs/limitations.md`.
""",
        "chart_map_title": "Insécurité alimentaire aiguë (IPC phase 3+), pays cibles",
        "chart_map_pct": "IPC phase 3+ (%)",
        "chart_map_people": "Personnes en phase 3+",
        "chart_map_disp": "Déplacés (accueillis)",
        "chart_map_u5": "Mortalité <5 ans",
        "chart_map_colorbar": "% en phase 3+",
        "chart_scatter_title": "Là où déplacement et faim se rejoignent",
        "chart_scatter_x": "Personnes déplacées accueillies (HCR)",
        "chart_scatter_y": "Population en phase IPC 3+ (%)",
        "chart_scatter_u5": "Mortalité <5 ans (pour 1000)",
        "chart_drill_p1": "Personnes en phase IPC 3+",
        "chart_drill_p2": "Déplacés accueillis",
        "chart_drill_p3": "Mortalité <5 ans vs médiane du panel",
        "chart_drill_bar_ipc": "Phase 3+",
        "chart_drill_bar_disp": "Déplacés",
        "chart_drill_median": "Médiane du panel",
        "chart_drill_title": "{country} en un coup d’œil",
        "chart_no_data": "Rien pour {iso3} pour l’instant",
        "chart_trends_p1": "Accueil (HCR)",
        "chart_trends_p2": "Mortalité <5 ans (OMS)",
        "chart_trends_series_disp": "Déplacés accueillis",
        "chart_trends_series_u5": "TMM <5 ans",
        "chart_trends_title": "{country} sur les années récentes",
        "country_gap": (
            "Nous n’avons pas trouvé d’estimation nationale actuelle IPC phase 3+ pour {country} "
            "dans cet extrait. Cela ne dit pas « pas de faim », seulement que cette tranche de "
            "données publiques est silencieuse. Lisez le déplacement et la mortalité infantile "
            "avec cette lacune en tête."
        ),
        "country_snapshot": (
            "Pour {country}, environ **{pct} %** de la population évaluée est en phase 3+, "
            "avec **{displaced}** personnes déplacées accueillies et une mortalité des moins "
            "de 5 ans autour de **{u5mr}** pour 1 000 naissances vivantes."
        ),
        "insight_headline": (
            "Double pression la plus élevée : {names} se situent à ou au-dessus des médianes "
            "du panel pour la part en phase IPC 3+ ({ipc_pct} %) et l’accueil de personnes "
            "déplacées ({displaced} personnes)."
        ),
        "insight_headline_empty": "Aucun pays ne se situe au-dessus des deux médianes dans cet extrait.",
        "insight_contrast": (
            " Note : {country} a une phase 3+ élevée ({ipc_pct} %), mais un accueil plus faible, "
            "faim et accueil ne disent pas la même chose."
        ),
        "insight_gap": (
            " Lacune : {names} {verb} pas de ligne IPC phase 3+ courante ici, "
            "donnée manquante, pas besoin nul."
        ),
        "insight_body_lead": (
            "Pour les équipes programme : commencez par le groupe sous double pression, "
            "puis parlez sécurité alimentaire et protection ensemble."
        ),
        "map_gap_note": (
            "**IPC manquant sur la carte : c’est volontaire.** {names} {verb} pas de ligne "
            "nationale *courante* en phase 3+ dans cet extrait. C’est une lacune de couverture, "
            "pas la preuve d’une absence de faim."
        ),
        "gap_verb_singular": "n’a",
        "gap_verb_plural": "n’ont",
    },
}

GLOSSARY = {
    "en": [
        ("IPC Phase 3+", "Integrated Food Security Phase Classification. Crisis or worse."),
        ("CoA / hosted", "Country of asylum, people received/hosted in that country."),
        ("CoO / origin", "Country of origin, where displaced people fled from (not used here)."),
        ("PoC", "Persons of concern to UNHCR (broader umbrella; we use REF+ASY+OOC)."),
        ("U5MR", "Under-five mortality rate (deaths per 1,000 live births), WHO GHO."),
        ("ISO3", "Three-letter country codes used to join all sources safely."),
    ],
    "fr": [
        ("IPC phase 3+", "Classification intégrée de la sécurité alimentaire. Crise ou pire."),
        ("Pays d’asile", "Personnes accueillies dans ce pays (approche retenue ici)."),
        ("Pays d’origine", "D’où les personnes ont fui (non utilisé ici)."),
        ("PdC / PoC", "Personnes relevant de la compétence du HCR (nous : REF+ASY+OOC)."),
        ("TMM <5 ans", "Taux de mortalité des moins de cinq ans (pour 1 000 naissances), OMS."),
        ("ISO3", "Codes pays à trois lettres pour joindre les sources."),
    ],
}

# Merge DE/IT/PT/ZH/RU packs
COPY.update(locales_extra.COPY)
GLOSSARY.update(locales_extra.GLOSSARY)

GAP_VERBS = {
    "en": ("has", "have"),
    "fr": ("n’a", "n’ont"),
    **locales_extra.GAP_VERBS,
}

for code, (sing, plur) in GAP_VERBS.items():
    if code in COPY:
        COPY[code].setdefault("gap_verb_singular", sing)
        COPY[code].setdefault("gap_verb_plural", plur)

NAV_KEYS = ("story", "map", "country", "about")


def t(lang: str, key: str, **kwargs) -> str:
    text = COPY.get(lang, COPY["en"]).get(key)
    if text is None:
        text = COPY["en"].get(key, key)
    if kwargs:
        return text.format(**kwargs)
    return text


def country_name(lang: str, iso3: str) -> str:
    names = FOCUS_NAMES_I18N.get(lang, FOCUS_NAMES_I18N["en"])
    return names.get(iso3, FOCUS_NAMES_I18N["en"].get(iso3, iso3))


def chart_labels(lang: str) -> dict[str, str]:
    keys = [
        "chart_map_title",
        "chart_map_pct",
        "chart_map_people",
        "chart_map_disp",
        "chart_map_u5",
        "chart_map_colorbar",
        "chart_scatter_title",
        "chart_scatter_x",
        "chart_scatter_y",
        "chart_scatter_u5",
        "chart_drill_p1",
        "chart_drill_p2",
        "chart_drill_p3",
        "chart_drill_bar_ipc",
        "chart_drill_bar_disp",
        "chart_drill_median",
        "chart_drill_title",
        "chart_no_data",
        "chart_trends_p1",
        "chart_trends_p2",
        "chart_trends_series_disp",
        "chart_trends_series_u5",
        "chart_trends_title",
    ]
    return {k: t(lang, k) for k in keys}
