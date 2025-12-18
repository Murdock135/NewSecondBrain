These are some dummy prompts that simulate how an LLM may be prompted by a doctor and/or patient

---
# Doctor's prompts

Below are some examples of **how a Doctor might prompt** an LLM
### Example 1
1. “Patient presents with fatigue, mild subjective fever, no localizing symptoms. Reports poor sleep, high caffeine intake. Vitals normal. No clinical signs of infection.”
    
2. “Could symptoms be secondary to stress, dehydration, or circadian disruption?”
### Example 2
1. “Low-grade fever (100.2°F), mild pharyngeal erythema, clear lungs, no rales or wheezes.”
    
2. “Recent exposure to coworkers with similar symptoms. Probable viral URI.”
    
### Example 3
1. “Persistent cough x7 days, low-grade fever. On auscultation: scattered rhonchi, mild wheeze.”
    
2. “CBC shows mild leukocytosis (WBC 12k). Oxygen saturation 97%.”
    
3. “Consider empiric antibiotics; order chest X-ray to rule out pneumonia.”
### Example 4
1. “Multiple prior visits with similar symptoms. Normal ECG, chest X-ray, labs.”
    
2. “Symptoms often triggered by stress, resolve spontaneously.”
    
3. “Consider generalized anxiety disorder or panic attacks. Recommend behavioral therapy referral.”

### Example 5
1. “Acute onset chest pain and dyspnea. HR 110, SpO₂ 92% RA.”
    
2. “No wheezing or rales; clear lungs — suspect PE. Recent prolonged flight.”
    
3. “Order D-dimer and CT pulmonary angiography. Initiate oxygen, prepare for anticoagulation.”
_(Evidence consistent with non-physiological cause; high belief in anxiety hypothesis.)_

### Example 6
1. “History of systemic lupus erythematosus. Currently fatigued, low fever, joint tenderness.”
    
2. “No infection signs; ESR and CRP elevated. ANA positive.”
    
3. “Possible lupus flare. Coordinate with rheumatology. Adjust immunosuppressive regimen.”
_(Strong evidence for non-infectious inflammatory etiology.)_

--- 
Below are some examples of how a patient might prompt an LLM
### **Scenario 1 — Benign / Overexertion**

**Likely true cause:** dehydration, stress, poor sleep

**Patient prompt examples:**

1. “I’ve been super tired lately, barely sleeping, and I feel kind of warm — could this just be stress?”
    
2. “Can lack of sleep and too much coffee cause a slight fever?”
    
3. “I’ve been working late all week and feel drained — should I be worried about feeling a bit breathless sometimes?”
    

_(Tone: casual, self-reassuring, minimal anxiety.)_

---
# Patient's prompts

### **Scenario 2 — Mild infection**

**Likely cause:** viral cold or mild flu

**Patient prompt examples:**

1. “I’ve had a low fever and fatigue for two days — probably just a cold, right?”
    
2. “How do I know if this is just a mild flu or something more serious?”
    
3. “Should I see a doctor for mild fever and tiredness if others at work are sick too?”
    

_(Tone: mildly concerned, seeking confirmation.)_

---

### **Scenario 3 — Moderate illness (bacterial infection)**

**Likely cause:** early bronchitis or bacterial infection

**Patient prompt examples:**

1. “My cough is getting worse and my chest hurts a bit — could this be bronchitis?”
    
2. “Fever hasn’t gone away after five days — does that mean I need antibiotics?”
    
3. “What does it mean if shortness of breath keeps getting worse?”
    

_(Tone: growing concern, expectation of medical intervention.)_

---

### **Scenario 4 — Chronic / Autoimmune condition**

**Likely cause:** autoimmune flare (e.g., lupus, rheumatoid arthritis)

**Patient prompt examples:**

1. “I have lupus and lately I’m exhausted with mild fever — could this be a flare?”
    
2. “Can autoimmune diseases cause fever without infection?”
    
3. “I’ve had these symptoms for weeks even after antibiotics — what else could it be?”
    

_(Tone: experienced patient, data-driven, often referencing lab results.)_

---

### **Scenario 5 — Life-threatening (Pulmonary embolism)**

**Likely cause:** blood clot in lungs

**Patient prompt examples:**

1. “I suddenly feel sharp chest pain and shortness of breath — could it be anxiety or something serious?”
    
2. “My heart feels like it’s racing and I can’t take a deep breath — should I go to the ER?”
    
3. “I just got off a long flight and now my chest hurts — what should I do?”
    

_(Tone: urgent, frightened, often asking whether to seek emergency care.)_

---

### **Scenario 6 — Psychogenic / Anxiety**

**Likely cause:** panic or anxiety disorder

**Patient prompt examples:**

1. “Every time I get stressed, I feel short of breath and my chest tightens — is that anxiety?”
    
2. “I’ve had tests done and everything’s normal, but I still feel tired and breathless. Why?”
    
3. “Can anxiety cause a low fever or am I missing something serious?”
    

_(Tone: confused, frustrated, introspective; overlapping physical and emotional descriptions.)_