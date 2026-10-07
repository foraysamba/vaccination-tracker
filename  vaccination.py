class Vaccine:
    def __init__(self, name, doses_required):
        self.name = name
        self.doses_required = doses_required

    def display_info(self):
        print(f"Vaccine: {self.name} | Doses required: {self.doses_required}")


class Recipient:
    # Class attribute (shared by all recipients)
    total_recipients = 0
    VALID_AGE_GROUPS = ("child", "adult", "senior")

    def __init__(self, recipient_id, age_group, vaccine):
        if not Recipient.is_valid_id(recipient_id):
            raise ValueError("ID must look like R001 (letter R + 3 digits).")
        if age_group not in Recipient.VALID_AGE_GROUPS:
            raise ValueError(f"Age group must be one of {Recipient.VALID_AGE_GROUPS}")
        self.recipient_id = recipient_id
        self.age_group = age_group
        self.vaccine = vaccine          # object interaction: Recipient has a Vaccine
        self.doses_received = 0
        Recipient.total_recipients += 1

    # ---- Instance methods ----
    def record_dose(self):
        """Record one dose, without exceeding the required number."""
        if self.doses_received < self.vaccine.doses_required:
            self.doses_received += 1
            return True
        return False

    def is_fully_vaccinated(self):
        return self.doses_received >= self.vaccine.doses_required

    def display_info(self):
        status = "Fully vaccinated" if self.is_fully_vaccinated() else "In progress"
        print(f"{self.recipient_id} | {self.age_group:<6} | {self.vaccine.name} | "
              f"{self.doses_received}/{self.vaccine.doses_required} doses | {status}")

    # ---- Class method  ----
    @classmethod
    def from_string(cls, text, vaccine):
        """Build a Recipient from a simple 'R001,adult' string."""
        recipient_id, age_group = text.split(",")
        return cls(recipient_id.strip(), age_group.strip(), vaccine)

    # ---- Static method  ----
    @staticmethod
    def is_valid_id(recipient_id):
        """Utility check - needs no access to class or instance data."""
        return (
            isinstance(recipient_id, str)
            and len(recipient_id) == 4
            and recipient_id[0] == "R"
            and recipient_id[1:].isdigit()
        )


# ---- Task 2: ONE data structure - a dictionary keyed by recipient ID ----
registry = {}


def add_recipient(recipient):
    """Add a recipient to the dictionary (ID is the key)."""
    if recipient.recipient_id in registry:
        print(f"ID {recipient.recipient_id} already exists - skipped.")
        return
    registry[recipient.recipient_id] = recipient


def display_all():
    """Loop through and display every record."""
    print("\n--- Vaccination Records ---")
    for recipient in registry.values():
        recipient.display_info()
    print(f"Total recipients: {Recipient.total_recipients}\n")


def main():
    # Object creation
    covid = Vaccine("COVID-19", 2)
    measles = Vaccine("Measles", 1)

    add_recipient(Recipient("R001", "adult", covid))
    add_recipient(Recipient("R002", "child", measles))
    add_recipient(Recipient.from_string("R003, senior", covid))  # class method

    # Object interaction: record doses
    registry["R001"].record_dose()
    registry["R002"].record_dose()
    registry["R003"].record_dose()
    registry["R003"].record_dose()

    display_all()

    # Static method demo
    print("Is 'R12' a valid ID?", Recipient.is_valid_id("R12"))
    print("Is 'R010' a valid ID?", Recipient.is_valid_id("R010"))


if __name__ == "__main__":
    main()
