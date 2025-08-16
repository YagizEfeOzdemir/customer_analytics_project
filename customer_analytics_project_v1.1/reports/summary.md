💡 Example – 01_CreditAmount_Duration_Pearson

---

## 1.1
**Test:** Pearson Correlation
**Hypotheses:**
- H₀: There is no linear relationship between the debt amount and maturity.
- H₁: There is a linear relationship between the debt amount and maturity.

---

#1.3
**Results:**
- Pearson r = 0.62
- p-value = 0.0001
- There is a positive, moderately significant relationship.

**Business Implication:**
- Customers generally prefer longer maturities when taking out larger loans.

---

💡 Example – 02_Age_Savings_Spearman

---

## 2.1
**Test:** Spearman Correlation
**Hypotheses:**
- H₀: There is no linear relationship between age and savings.
- H₁: There is a linear relationship between age and savings.

---

#2.3
**Results:**
- Pearson r = 0.10
- p-value = 0.00214
- There is a small but positive, moderately significant relationship.

**Business Implication:**
-  As age increases, there is a slight tendency for individuals to belong to higher savings categories.

---

💡 Example – 03_InstallmentRate_CreditAmount_Spearman

---

## 3.1
**Test:** Spearman Correlation
**Hypotheses:**
- H₀: There is no linear relationship between the installment rate and the credit amount.
- H₁: There is a linear relationship between the installment rate and the credit amount.

---

#3.3
**Results:**
- Spearman r = -0.31
- p-value = 0.00000
- Moderate negative and highly significant relationship.

**Business Implication:**
- Higher installment rates tend to be linked with smaller credit amounts.

---

💡 Example – 04_Purpose_CreditHistory_Chi2

---

## 4.1
**Test:** Chi-Square Test
**Hypotheses:**
- H₀: Purpose and CreditHistory are independent.
- H₁: Purpose and CreditHistory are not independent.

---

# 4.3
**Results:**
- Chi² = 111.70
- p-value = 0.00000
- dof = 36
- Strong evidence against H₀ → Purpose and CreditHistory are **not independent**.

**Business Implication:**
- Customers’ credit purpose is strongly associated with their credit history.
  For example, certain purposes (like car loans or business loans) tend to occur more often among customers with specific credit history patterns.

---

💡 Example – 05_Target_Duration_Ztest

---

## 5.1
**Test:** Z Test
**Hypotheses:**
- H₀: There is no statistically significant difference in the average loan duration between good and bad customers.
- H₀: There is a statistically significant difference in the average loan duration between good and bad customers.

---

# 5.3
**Results:**
- Z = -6.9523
- p-value = 0.00000
- Strong evidence against H₀ → There is a statistically significant **difference** in the average loan duration between good and bad customers.


**Business Implication:**
- Loan duration is strongly associated with credit status.
- Customers with bad credit tend to have longer loan durations on average, which may indicate higher repayment risk and require stricter lending policies.

---

💡 Example – 06_Target_CreditAmount_t_test

---

## 6.1
**Test:** t Test
**Hypotheses:**
- H₀: There is no statistically significant difference in the average credit amount between good and bad customers.
- H₀: There is a statistically significant difference in the average credit amount between good and bad customers.

---

**6.3**
**Results:**
- t-score = -4.9480
- p-value = 0.00000
- Strong evidence against H₀ → Average credit amount differs significantly between good  and bad customer groups.

**Business Implication:**
- Credit amount is associated with credit status.
- Customers with bad credit may have higher/lower credit amounts, influencing loan risk assessment and credit limit decisions.

---

💡 Example – 07_CreditAmount_Outlier_test

---

**7.1**
- **Test: Outlier Detection (IQR Method)**
- **Hypotheses:**
- This step does not involve a statistical hypothesis test. Instead, it applies the Interquartile Range (IQR) method to identify unusually high or low credit amounts that may be considered outliers.

---

**7.3**
**Result:**
- The first quartile (Q1) was 1365.5 and the third quartile (Q3) was 3972.25, giving an IQR of 2606.75.
- The calculated lower bound was -2544.625 (no outliers detected below this value) and the upper bound was 7882.375.
- A total of 72 credit amounts exceeded the upper bound and were classified as outliers. These represent customers with unusually high credit amounts compared to the majority of the dataset.

---

**7.3**
**Result:**
- The first quartile (Q1) was 1365.5 and the third quartile (Q3) was 3972.25, giving an IQR of 2606.75.
- The calculated lower bound was -2544.625 (no outliers detected below this value) and the upper bound was 7882.375.
- A total of 72 credit amounts exceeded the upper bound and were classified as outliers. These represent customers with unusually high credit amounts compared to the majority of the dataset.