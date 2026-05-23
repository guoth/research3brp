from otree.api import Bot, expect

from . import *


def estimate_payload():
    payload = {f'estimate_actual_{i}': 0 for i in range(21)}
    payload.update({f'estimate_should_{i}': 0 for i in range(21)})
    payload['estimate_actual_0'] = 100
    payload['estimate_should_0'] = 100
    payload['estimate_reaction_time'] = 1
    return payload


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            expect(self.player.current_logic, 1)
            yield ConsentPage, dict(consent=True)
            yield ParticipantID, dict(subject_id=1001)
        else:
            expect(self.player.current_logic, 2)

        yield Instructions, dict(
            comprehension_answer=23,
            comprehension_answer_e=21,
        )
        yield EstimateOthers, estimate_payload()
        yield Contribute, dict(
            contribution=1,
            transfer_to_e=1,
            reaction_time=1,
            page_load_time=1,
        )

        if self.round_number == 2:
            yield QuestionnairePart1, dict(
                major='Psychology',
                major_category='其他',
                student_id='20260001',
                gender='女',
                age=20,
                education='大学本科',
                work_experience='否',
            )
            yield QuestionnairePart2, dict(is_real_player='是真人')

        yield Results
