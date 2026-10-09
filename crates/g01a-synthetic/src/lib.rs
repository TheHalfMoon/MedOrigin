#![forbid(unsafe_code)]
//! Synthetic-only reproducibility substrate. This is not a clinical engine.

/// The fixture is compiled into the binary; no runtime filesystem or network is used.
pub const FIXTURE: &str = include_str!("../../../fixtures/g01a_synthetic_v1.txt");

/// Deliberately conservative, constant governance classifications.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct SyntheticReceipt {
    pub classification: &'static str,
    pub clinical_validation: &'static str,
    pub source_imports: &'static str,
    pub data_rights: &'static str,
    pub fixture_bytes: usize,
}

pub fn receipt() -> SyntheticReceipt {
    SyntheticReceipt {
        classification: "SYNTHETIC_ONLY",
        clinical_validation: "NOT_PERFORMED",
        source_imports: "BLOCKED",
        data_rights: "NO_ADMISSIONS",
        fixture_bytes: FIXTURE.len(),
    }
}

pub fn render_receipt() -> String {
    let r = receipt();
    format!(
        "classification={}\nclinical_validation={}\nsource_imports={}\ndata_rights={}\nfixture_bytes={}\n",
        r.classification, r.clinical_validation, r.source_imports, r.data_rights, r.fixture_bytes,
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn receipt_is_deterministic_and_nonclinical() {
        let a = receipt();
        assert_eq!(a, receipt());
        assert_eq!(a.classification, "SYNTHETIC_ONLY");
        assert_eq!(a.clinical_validation, "NOT_PERFORMED");
        assert_eq!(a.source_imports, "BLOCKED");
        assert_eq!(a.data_rights, "NO_ADMISSIONS");
    }

    #[test]
    fn fixture_contains_only_frozen_synthetic_markers() {
        assert!(FIXTURE.is_ascii());
        assert!(FIXTURE.starts_with("SAFE_EVIDENCE_G01A_SYNTHETIC_ONLY_V1\n"));
        assert!(FIXTURE.contains("NO_PATIENT_DATA\n"));
        assert!(FIXTURE.contains("NO_CLINICAL_EVIDENCE\n"));
        assert!(FIXTURE.contains("NO_SOURCE_IMPORTS\n"));
        assert_eq!(receipt().fixture_bytes, FIXTURE.len());
    }

    #[test]
    fn rendered_receipt_cannot_claim_validation_or_imports() {
        let output = render_receipt();
        assert!(output.starts_with("classification=SYNTHETIC_ONLY\n"));
        assert!(output.contains("clinical_validation=NOT_PERFORMED\n"));
        assert!(output.contains("source_imports=BLOCKED\n"));
        assert!(output.contains("data_rights=NO_ADMISSIONS\n"));
        assert!(!output.contains("APPROVED"));
    }
}
