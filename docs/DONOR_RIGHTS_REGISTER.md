# SafeEvidence Donor Rights Register

Status: `P00_BINDING`

Founder statement: permission has been asserted for all discussed source-code
donors. This register does not deny that assertion. It makes the permission
basis auditable before copying bytes into SafeEvidence.

## Admission basis

- `PUBLIC_LICENSE`
- `FOUNDER_OWNED`
- `SEPARATE_PERMISSION_ASSERTED`
- `SEPARATE_PERMISSION_VERIFIED`
- `REFERENCE_ONLY_PENDING_RIGHTS`
- `DENIED`

Code, models, datasets, terminology, publications, fonts and other assets are
tracked separately.

## Initial register

| Source | Current planning basis | Default allowed mode before further record |
|---|---|---|
| TheHalfMoon/MedScale | PUBLIC_LICENSE / founder-controlled sibling | COPY_BOUNDED / DEPEND after slice review |
| TheHalfMoon/DAL | PUBLIC_LICENSE / founder-controlled sibling | COPY_BOUNDED |
| TheHalfMoon/commandMed | PUBLIC_LICENSE / founder-controlled sibling | ORACLE_COPY / COPY_BOUNDED |
| TheHalfMoon/MESC | founder-controlled sibling; exact file licenses required | REFERENCE / COPY after slice record |
| TheHalfMoon/Morize | founder-controlled sibling; exact file licenses required | REFERENCE / COPY after slice record |
| TheHalfMoon/ottari | founder-controlled sibling; exact file licenses required | COPY_BOUNDED after slice record |
| TheHalfMoon/kernux | founder-controlled sibling; exact file licenses required | COPY_BOUNDED after slice record |
| TheHalfMoon/Signthos | AGPL public tree plus founder permission assertion | REFERENCE until separate permission/relicense record is attached |
| AbdulazizShehri/SafeOCR | Apache-2.0 at inspected state | COPY_BOUNDED after dependency/model review |
| maziyarpanahi/openmed | public license plus per-data/model gates | COPY_BOUNDED / DEPEND; restricted assets excluded |
| xberg-io/xberg | public license plus transitive/native/model review | DEPEND / VENDOR after feature/rights closure |
| docling-project/docling.rs | public license plus model review | DEPEND / VENDOR after feature/rights closure |
| fastembed-rs | PUBLIC_LICENSE | DEPEND / VENDOR |
| ncbi/MedCPT | code basis recorded separately from model weights | REFERENCE / ARTIFACT_IMPORT after model-card admission |
| ASReview | PUBLIC_LICENSE | WORKER / COPY_BOUNDED |
| SYNERGY | dataset terms tracked separately | BENCHMARK after item/data-rights review |
| UniFFI | PUBLIC_LICENSE with covered-file obligations | DEPEND |
| tough / rust-tuf | PUBLIC_LICENSE | DEPEND after conformance qualification |
| cqframework CQL | PUBLIC_LICENSE | WORKER / REFERENCE |
| HL7/ebm | standards/reference terms | REFERENCE / EXPORT_CROSSWALK |
| SciFact | code/data terms tracked separately | BENCHMARK / CODE_REFERENCE |
| MultiVerS | public repo; exact code/model rights required | BENCHMARK_ONLY until admitted |
| evidence-surveillance/es3 | public license at inspected revision | COPY_BOUNDED / REFERENCE |
| trialstreamer | founder asserts separate permission; no public license observed | REFERENCE_ONLY_PENDING_RIGHTS until permission reference is recorded |
| robotreviewer | GPL public tree; founder asserts separate permission | BENCHMARK/WORKER until separate permission or GPL distribution decision is recorded |
| RRnlp | code/model rights reviewed separately | BENCHMARK / MODEL_ARTIFACT_IMPORT after admission |
| Evidence Inference | code/data/publication rights separate | BENCHMARK / COPY_BOUNDED after data-rights review |
| PICOX | notebook/data/model rights separate | BENCHMARK / REFERENCE |
| statsmodels | PUBLIC_LICENSE | DEPEND / VENDOR_SELECTED |
| metafor | copyleft R package | DEVELOPMENT_ORACLE / OPTIONAL_WORKER subject to distribution decision |
| Slint | custom/GPL/commercial choices | DEPEND only after selected license/attribution record |
| Tauri | public permissive license | DEPEND candidate |
| Iroh | exact adopted license/revision required | DEPEND candidate after transport qualification |

## Import rule

No external source with `SEPARATE_PERMISSION_ASSERTED` or
`REFERENCE_ONLY_PENDING_RIGHTS` may be copied into the Apache-2.0 product tree
until the repository records a documentary permission reference or an allowed
public-license path.

A permission record must identify:
- rightsholder/grant source;
- covered repository/revision or scope;
- allowed modification/redistribution/rebranding;
- sublicensing/combined-work constraints where relevant;
- required notices.

Public code permission never implies permission for model weights, datasets,
terminology or publication content.
