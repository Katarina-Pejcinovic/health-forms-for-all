# Form This Way

**Form This Way** is a PDF processor for medical intake forms to use more
inclusive language. It was made for [QWER Hacks 2023](https://www.qwerhacks.com)
([submission here](https://devpost.com/software/form-this-way)) for the
following categories:
* **Healthcare Equity track**
* Best Technical
* Most Innovative
* Comeback Baby
* Best Idea
* Most Slayful UI

![Form This Way Logo - Lady Gaga's Eye](examples/pymupdf-example/logo-dark.png)

## About

The LGBTQ+ population is at disproportionate risk for numerous medical risks
including chronic diseases such as asthma, diabetes, and heart disease; mental
health conditions; and substance abuse. At the same time, they have lower rates
of healthcare access and utilization. This may be attributed to fear of
discrimination from healthcare providers and the stigmas surrounding the LGBTQ+
community in the medical setting.

For many, microaggressions begin even before meeting with the physician. Patient
intake forms being used in modern clinical practice use outdated and non
inclusive terms that prevent medical practitioners from gathering important
patient information and can make patients hesitant to share personal
information. Historically, this has led to worse outcomes for patients of sexual
and gender minority. 

Adopting inclusive medical practices at all levels will promote feelings of
security and acceptance for members of the LGBTQ+ community, foster stronger
patient-physician relationships, and improve overall quality and continuity of
care. Our application serves as a tool to aid the implementation of inclusive
language and educate on the importance of this language in the medical setting.

Citations: [[1]](https://doi.org/10.1016/j.radi.2016.04.011)
[[2]](https://doi.org/10.1016/j.echu.2019.08.005)
[[3]](https://doi.org/10.1371/journal.pone.0146139)

## System requirements

Form This Way requires [Python](https://www.python.org) to run. It also requires
the following Python packages:
* `PyMuPDF`
* `tk`
* `Pillow`

If you have Python installed, here is a quick way to setup the repository and
ensure you have all the dependencies:
```
git clone https://github.com/Katarina-Pejcinovic/health-forms-for-all.git
pip install PyMuPDF tk Pillow
```
## Running the app

Once you have the repository cloned:
```
cd examples/pymupdf-example
python guiFile.py
```
If the `python` command throws an error, try `python3` or checking which Python
interpreter you're using.
