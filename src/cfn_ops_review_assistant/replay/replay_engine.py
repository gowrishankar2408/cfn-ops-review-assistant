class ReplayEngine:

    def execute(
        self,
        capability,
        case_number,
        token,
    ):

        print(
            f"Executing capability "
            f"{capability.name} "
            f"v{capability.version}"
        )

        return capability.execute(
            case_number,
            token,
        )