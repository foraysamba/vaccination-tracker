Vaccination Tracker
A small Python OOP program that tracks vaccination progress for anonymous recipients.
Problem
Health workers need a simple way to see who has completed their vaccine doses,
without storing sensitive personal information.
How to run
python vaccination_tracker.py
Requires Python 3.8+. No external libraries.
Example usage
The program creates sample recipients, records doses, and prints the registry.
Sample code (inside main()):
covid = Vaccine("COVID-19", 2)
add_recipient(Recipient("R001", "adult", covid))
add_recipient(Recipient.from_string("R003, senior", covid))
registry["R001"].record_dose()
display_all()
print(Recipient.is_valid_id("R12"))
Sample output (full program):
--- Vaccination Records ---
R001 | adult  | COVID-19 | 1/2 doses | In progress
R002 | child  | Measles | 1/1 doses | Fully vaccinated
R003 | senior | COVID-19 | 2/2 doses | Fully vaccinated
Total recipients: 3

Is 'R12' a valid ID? False
Is 'R010' a valid ID? True
OOP concepts used
Concept
Where
Classes and objects
Vaccine, Recipient
Attributes
recipient_id, age_group, doses_received, name, doses_required
Instance methods
record_dose(), is_fully_vaccinated(), display_info()
Class method
Recipient.from_string()
Static method
Recipient.is_valid_id()
Class attribute
Recipient.total_recipients
Data structure
One dictionary (registry), keyed by recipient ID
Digital Public Goods (DPG) alignment
Open-source: code is published on GitHub under an open license (MIT).
Privacy-respecting: no names or sensitive data; only anonymous IDs and age groups.
Inclusive and accessible: plain-text output, simple English, no special hardware or internet needed.
Modular and reusable: each class has one job; Vaccine can be reused for any vaccine and the tracker adapted to other health programs.
License
MIT