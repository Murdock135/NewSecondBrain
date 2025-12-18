Extracting hypotheses and belief masses from natural language would, besides its own obvious benefit, would allows us to also look at certain types of biases. For example, for the the same prompt "family" $P$, if one prompt has the word "boy" in it and another has "girl" in it, and if the hypotheses and/or the belief masses extracted are different, that will expose biases. 

---
# Approach 1
**Using NLI and DST/fuzzy**

After getting the LLM outputs, we ask another LLM to extract the premises and synthesize hypotheses. The hypotheses will be *partially fixed*; It will have a particular structure, but with variables. The variables will be replaced by the elements from the universe of discourse. Take the following example:

---
**Input**:
these are my notes on a patient:
1. “History of systemic lupus erythematosus. Currently fatigued, low fever, joint tenderness.”

2. “No infection signs; ESR and CRP elevated. ANA positive.”

---

**Output:**
Thank you for sharing your notes. Here’s a general **educational interpretation** of the findings based on current evidence-based medical knowledge, without offering patient-specific clinical advice:

**Systemic Lupus Erythematosus (SLE): Possible Flare vs. Other Etiologies**
 **1. Clinical Presentation**

- **Fatigue, low-grade fever, and joint tenderness** are **common features of SLE flare**.
    
- Absence of infection signs helps **reduce (but not exclude)** the likelihood of infectious etiologies.
 **2. Laboratory Findings**
- **Elevated ESR and CRP**:
    
    - **ESR** is frequently elevated in both SLE flares and infections.
        
    - **CRP**, however, tends to be **normal or only mildly elevated in SLE flares**, and **markedly elevated in infections or inflammatory conditions like serositis** or **lupus arthritis**.
        
    
- **Positive ANA**:
    
    - Not specific to flare activity but supports the **diagnosis of SLE**.
        
    - ANA titers do not typically correlate with disease activity.

 **3. Differential Diagnosis**
While a flare is a leading consideration, other possibilities include:

- **Infection** (despite no overt signs): Rule out via cultures or imaging if clinically indicated.
    
- **Drug-induced symptoms**: Certain medications in SLE patients (e.g., immunosuppressants) can cause fever or fatigue.
    
- **Other autoimmune processes** (e.g., overlap syndromes like RA/SLE).
    
- **Malignancy or hematologic disorders** (especially if cytopenias or constitutional symptoms appear).
    

  

 **Next Steps (Educational Only)**
 
In the general management of suspected SLE flares, clinicians may:

- Assess for **other markers of disease activity**: dsDNA, complement (C3/C4), urine protein/creatinine ratio.
    
- Evaluate organ involvement: renal (UA, creatinine), CNS, hematologic.
    
- Consider imaging or cultures to definitively exclude infections.
    

 **Key Points**

- Fever and fatigue in an SLE patient should prompt consideration of a **flare**, but **infection must always be ruled out**, especially in immunosuppressed individuals.
    
- **CRP disproportionately high** to ESR may point toward infection or another inflammatory condition.
    
- Laboratory trends (complement levels, dsDNA) help **assess flare activity** more specifically than ANA.
    


**Confidence Estimate:** High for general principles; based on current SLE management guidelines (e.g., 2019 EULAR/ACR Criteria for SLE, UpToDate, accessed October 2025).

**Sources:**

- EULAR/ACR Classification Criteria for SLE. _Ann Rheum Dis_ 2019;78:1151–1159.
    
- UpToDate: “Clinical manifestations and diagnosis of systemic lupus erythematosus in adults.” Accessed October 2025.
    

Let me know if you’d like a differential table or further guidance on distinguishing SLE flare from infection or other mimics.

---
From this, we would extract its hypotheses. We would do the same for all other LLMs and use NLI to determine which hypotheses are entailments, contradictions and neutrals. This basically yields information conflicts and agreements. However, this does not yield partial conflicts.