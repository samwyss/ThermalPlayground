from typing import Any


class Config:
    """configuration object"""

    def __init__(
        self,
        fuel_thickness: float,
        cladding_thickness: float,
        bulk_material_temp: float,
        coolant_temp: float,
        core_heat_generation: float,
        num_saved_time_steps: int,
    ):
        """
        Config constructor
        :param fuel_thickness: [m] fuel thickness
        :param cladding_thickness: [m] cladding thickness
        :param bulk_material_temp: [K] bulk material temperature
        :param coolant_temp: [K] coolant temperature
        :param core_heat_generation: [W/m^3] core heat generation
        :param num_saved_time_steps: [] number of saved time steps
        """
        self.__fuel_thickness: float = fuel_thickness
        """[m] fuel thickness"""

        self.__cladding_thickness: float = cladding_thickness
        """[m] cladding thickness"""

        self.__bulk_material_temp: float = bulk_material_temp
        """[K] bulk material temperature"""

        self.__coolant_temp: float = coolant_temp
        """[K] coolant temperature"""

        self.__core_heat_generation: float = core_heat_generation
        """[W/m^3] core heat generation"""

        self.__num_saved_time_steps: int = num_saved_time_steps
        """[] number of saved time steps"""

    def __repr__(self) -> dict[str, Any]:
        """modifies how Config is displayed"""
        return self.__dict__

    def get_fuel_thickness(self) -> float:
        """
        fuel thickness getter
        :return: fuel thickness
        """
        return self.__fuel_thickness

    def get_cladding_thickness(self) -> float:
        """
        cladding thickness getter
        :return: cladding thickness
        """
        return self.__cladding_thickness

    def get_bulk_material_temp(self) -> float:
        """
        bulk material temperature getter
        :return: bulk material temperature
        """
        return self.__bulk_material_temp

    def get_coolant_temp(self) -> float:
        """
        coolant temperature getter
        :return: coolant temperature
        """
        return self.__coolant_temp

    def get_core_heat_generation(self) -> float:
        """
        core heat generation getter
        :return: core heat generation
        """
        return self.__core_heat_generation

    def get_num_saved_time_steps(self) -> int:
        """
        number of saved time steps getter
        :return: number of saved time steps
        """
        return self.__num_saved_time_steps
