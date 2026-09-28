'''PPS Custom Expiration Review Process'''


class PPSCustomExpirationReview:

    def execute(
        self,
        case_number: str,
        token: str,
    ):

        print(
            f"Running PPS Custom Expiration Review "
            f"for {case_number}"
        )