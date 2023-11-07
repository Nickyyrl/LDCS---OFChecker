# LDCS - OpenFields Checker

![LDCS - OpenFields Checker](https://raw.githubusercontent.com/Nickyyrl/LDCS---OFChecker/main/Templates/logo_ldcs-removebg-preview.ico)

LDCS - OpenFields Checker is a Python web application built with Flask that allows you to check the similarity of elements in a CSV file to a specific pattern using the Jaro-Winkler similarity metric. This documentation provides information on how to install and use the program.

## Installation 

### Requirements 

Before installing the program, make sure you have the following prerequisites:

- Python 3.10 or higher installed on your system.
- `pip` (Python package manager) installed.


### Installation Steps / Windows 

With Git :

1. **Clone the Repository**:

   > git clone https://github.com/Nickyyrl/LDCS---OFChecker

   Or 

   > download last version : [LDCS-OFChecker](https://github.com/Nickyyrl/LDCS---OFChecker)

2. Unzip Folder

3. install  requierements.txt by clicking on installer.bat

## Usage / Utilisation

### Dashboard

The main dashboard of the application allows you to perform the following actions:

- **Load Patterns / Charger des motifs**:
  - Load predefined patterns from the patterns.txt file.

- **Set Pattern / Définir un motif**:
  - Set a new pattern or select an existing one.

- **Set Tolerance / Définir une tolérance**:
  - Set a similarity tolerance level for pattern matching.

- **Upload a CSV File / Télécharger un fichier CSV**:
  - Upload a CSV file for similarity analysis.

- **Reset Tool / Réinitialiser l'outil**:
  - Reset the tool's statistics and results.

### Pattern Matching / Correspondance de motifs

1. **Load Patterns / Charger des motifs**:

   You can load predefined patterns from the patterns.txt file. This step is optional and can help you quickly select patterns for analysis.

2. **Set Pattern / Définir un motif**:

   You can set a specific pattern for similarity analysis by typing it in the input field or selecting an existing pattern from the dropdown.

3. **Set Tolerance / Définir une tolérance**:

   Set the similarity tolerance level using the input field. This value determines how similar elements in the CSV file should be to the selected pattern to be considered valid.

4. **Upload a CSV File / Télécharger un fichier CSV**:

   Upload a CSV file for analysis. The application will calculate the Jaro-Winkler similarity between the elements in the CSV file and the selected pattern.

5. **Reset Tool / Réinitialiser l'outil**:

   Clicking this button will reset the tool's statistics, including valid and invalid counts.

### Results 

After uploading a CSV file and initiating the analysis, you will see the following information on the dashboard:

- **Elements Tested / Éléments testés**:
  - The total number of elements in the CSV file that were analyzed.

- **Last Element / Dernier élément**:
  - The most recent element that was analyzed.

- **Last Score / Dernier score**:
  - The Jaro-Winkler similarity score of the last analyzed element.

- **Average Score / Score moyen**:
  - The average Jaro-Winkler similarity score of all analyzed elements.

- **Valid Count / Compteur valide**:
  - The number of elements with a similarity score higher than or equal to the set tolerance.

- **Invalid Count / Compteur invalide**:
  - The number of elements with a similarity score lower than the set tolerance.

### Export Results 

You can export the analysis results to a CSV file by clicking the "Export Results" button. The exported CSV file will contain a list of all elements and their similarity scores.

## Patterns 

Patterns are used for similarity analysis. You can load predefined patterns from the patterns.txt file or set new patterns through the application.

## Saving Patterns 

If you want to save patterns for future use, you can manually add them to the patterns.txt file in the following format:

```plaintext
Pattern 1
Pattern 2
Pattern 3
...
```

Each pattern should be on a separate line.

### Conclusion
LDCS - OpenFields Checker is a powerful tool for analyzing the similarity of elements in a CSV file to specific patterns. It can be useful for various data analysis and validation tasks.

Version : Beta-3.0.1

### Fixes 

- 