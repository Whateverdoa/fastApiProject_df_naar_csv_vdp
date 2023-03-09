from dataclasses import dataclass
from datetime import datetime

from enum import Enum
from pathlib import Path
import math


@dataclass(kw_only=True)
class InputOrder:
    mes: int
    invoer_aantal_vdps: int
    etiket_y: int
    name_file_invoer: Path
    sluitbarcode_uitvul_waarde: int
    sluitbarcode_posities: int
    extra_etiketten: int
    hoogte: float
    kern_diameter: int
    opmerkingen: str
    soortsluit_etiket: bool
    wikkel_keuze: bool
    aantal_van_rol_overlevering_procent: int
    aantal_van_rol: int
    aantal_overlevering_choice: bool
    aantal_per_rol: int  # komt uit geladen file dus andere class
    aantal_rollen: int

    @property
    def sluitbarcode_uitvul_waarde_getal(self, ) -> str:
        return f"{self.sluitbarcode_uitvul_waarde:>{0}{self.sluitbarcode_posities}}"

    @property
    def amount_with_percentage(self) -> int:
        result = self.aantal_van_rol * (1 + self.aantal_van_rol_overlevering_procent / 100)
        return int(result)

    @property
    def wikkel(self):
        """kiest tussen handmatig en formule"""

        pi = math.pi

        materiaal = 145  # global var
        var_1 = int(
            math.sqrt(
                (4 / pi) * ((self.aantal_per_rol * self.formaat_hoogte) / 1000) * materiaal
                + pow(self.kern_diameter, 2)
            )
        )
        de_wikkel = int(2 * pi * (var_1 / 2) / self.formaat_hoogte + 2)
        return de_wikkel

    @property
    def aantal_per_rol_calculated(self):
        if self.aantal_overlevering_choice:
            return self.aantal_van_rol + self.extra_etiketten
        else:

            return self.amount_with_percentage


@dataclass(kw_only=True)
class Job:
    OrderId: str
    SubOrderId: str

    OrderYear: str
    Name: str
    Description: str
    DueDate: str
    JobStatus: str
    ProjectId: str
    Category: str
    Proof: str
    Dispenser: str
    LabelDirection: str
    Adhesive: str
    Size: str
    JobFolder: str
    JobType: str
    Handling: str
    QOrder: str




@dataclass(kw_only=True)
class Customer:
    CustomerId: str
    CustomerName: str
    CustomerDescription: str
    CustomerJobReference: str
    JobHandler: str
    JobHandlerEmail: str


@dataclass(kw_only=True)
class Template:
    UseExistingTemplate: bool
    JobTemplate: str


@dataclass(kw_only=True)
class Parameter:
    Radius: str
    DieCut2_LabelsAcross: str
    DieCut2_LabelsAlong: str
    DieCut2_GutterAcross: str
    DieCut2_GutterAlong: str
    DieCut2_RepeatLength: str
    ProofsLogo: str
    ProofsLanguage: str
    JobQuantity: str
    QuantityPerRoll: str
    Substrate: str
    CustomerFirstLetter: str


@dataclass(kw_only=True)
class Eskoproduct:
    ProductNo: str
    ProductName: str
    EskoDescription: str
    CustomerName: str
    CustomerFirstLetter: str
    CustomerNo: str
    CustomerProductReference: str
    LabelWidth: str
    LabelHeight: str
    LabelSize: str
    Department: str
    Description: str
    Shape: str
    LabelDirection: str
    Colours: str
    Status: str
    Core: str
    Notes: str


testInputOrder = InputOrder(mes=3,
                            invoer_aantal_vdps=1,
                            etiket_y=11,
                            name_file_invoer=Path('a'),
                            sluitbarcode_uitvul_waarde=0,
                            sluitbarcode_posities=8,
                            hoogte=80,
                            kern_diameter=76,
                            opmerkingen="geen opmerkingen",
                            soortsluit_etiket=False,
                            wikkel_keuze=False,
                            aantal_overlevering_choice=True,
                            extra_etiketten=10,
                            aantal_van_rol=1000,
                            aantal_van_rol_overlevering_procent=10,
                            aantal_per_rol=500,
                            aantal_rollen=2,
                            )
