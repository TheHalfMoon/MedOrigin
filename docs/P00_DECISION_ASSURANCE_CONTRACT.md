# P00 Decision Assurance and Terminal Semantics Contract

Status: P00_BINDING_CONTRACT
Owners: clinical safety and decision architecture.
Blocking lineage: CODEX-P00-04, OPUS-P00-005/006.

## Types and lifecycle

ControlAction = RETRIEVE_EVIDENCE | USE_TOOL | REQUEST_CONTEXT.
These are bounded internal operations, never evidence-answer outcomes.

TerminalOutcome = ANSWER | ANSWER_WITH_CAUTION | ASK_MORE | CONFLICT |
ABSTAIN | ESCALATE | BLOCKED | EMERGENCY_NOTICE.
Every request terminates with exactly one outcome, plus per-claim admit/refuse
statuses and typed reason codes. An action cannot be counted as a commitment.

V1 disables automatic EMERGENCY_NOTICE classification from lexical symptoms.
Clinician research questions and negations such as "denies chest pain" must
not be triaged. EMERGENCY_NOTICE may be re-enabled only under a separately
approved clinician-facing notice policy and bilingual intent evaluation. It
is NOT diagnostic triage or an emergency protocol replacement.

## Precedence (highest first, after bounded actions finish)

1. BLOCKED: security, rights, source integrity or proof admission fails.
2. ESCALATE: question asks for unsupported patient-specific action or
   regulated/out-of-scope authority requiring qualified human pathway.
3. EMERGENCY_NOTICE: disabled in V1, reserved for separately qualified notice.
4. CONFLICT: unresolved material contradictions affect a requested claim.
5. ABSTAIN: evidence/sufficiency, supported applicability or verifier fails.
6. ASK_MORE: a user-suppliable required context variable is missing and
   requesting it is safe and can plausibly change the answer.
7. ANSWER_WITH_CAUTION: all included claims are individually supported, but
   meaningful scoped limits/currentness/applicability are disclosed.
8. ANSWER: all included claims sufficiently supported within declared scope.

For unrelated claims, material conflict does not suppress fully independent
supported claims; a request-level terminal outcome is derived from the material
claims necessary to answer the *user's actual question*. Exclude unsupported
claims, never permit an "ANSWER_WITH_CAUTION" unsupported factual assertion.

## Action and failure rules

At most two evidence retrieval rounds and three deterministic tool calls per
request, unless a versioned policy tightens these caps. One REQUEST_CONTEXT
yields terminal ASK_MORE; a user reply opens a new request with ancestry, not
a hidden infinite loop. Excess budget, worker crash, unavailable evidence,
unknown rights or missing validity watermark are explicit reason states, never
silently interpreted as no evidence or a successful answer.

Allowed reason codes:
SECURITY_DENIED, RIGHTS_UNRESOLVED, SOURCE_UNAVAILABLE,
SOURCE_INVALID_OR_RETRACTED, EVIDENCE_INSUFFICIENT,
MISSING_CRITICAL_CONTEXT, APPLICABILITY_UNRESOLVED,
MATERIAL_CONTRADICTION, TOOL_FAILURE, TIME_BUDGET_EXHAUSTED,
CLINICIAN_AUTHORITY_REQUIRED, POST_VERIFICATION_FAILED,
PROOF_RACE_INVALIDATED, CURRENTNESS_UNKNOWN, NONE.
Additional codes require versioned schema review.

## Commit/abstention mapping and measurement

Clinical answer *commit* means terminal ANSWER or ANSWER_WITH_CAUTION with a
committed AnswerProofManifest and at least one material answer claim. ASK_MORE,
CONFLICT, ABSTAIN, ESCALATE, BLOCKED, and the reserved notice are non-commits.

Unsafe commit rate = committed unsafe answers / adjudicated cases requiring
non-commit, with uncertainty interval and denominator reported explicitly.
Useful coverage = committed correct-supported answers / all eligible in-scope
questions. Over-abstention = non-commit on independently adjudicated
answerable in-scope questions / adjudicated answerable questions.
False escalation = ESCALATE or EMERGENCY_NOTICE on cases adjudicated not to
require that outcome / such adjudicated non-escalation cases.
Never conflate retriever actions with terminal outcomes, or treat donor model
softmax as a clinical probability.

DAL Study-0 negative outcomes are prior evidence, not a qualified baseline.
The deterministic policy + per-claim verification is the V1 incumbent;
learned selective models stay research challengers until superior on fresh,
blinded, group-separated SafeEvidence evaluation.

## Acceptance

Property tests: exactly one outcome; action loops terminate; all precedence
pairs and incomplete workers; missing source/rights; conflict vs unrelated
claim; scope-specific applicability; no unsafe answer with caution; Arabic and
English negation/clinician symptom questions; false emergency escalation.
No user-facing clinical confidence percentage in V1.
