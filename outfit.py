import arrow

class BattleRank:

    def __init__(self, percent_to_next: str, value: str):
        self.percent_to_next = float(percent_to_next)
        self.value = int(value)

class CertificationPoints:

    def __init__(self, available_points:str, earned_points:str, gifted_points:str, percent_to_next:str, spent_points:str):
        self.available_points = int(available_points)
        self.earned_points = int(earned_points)
        self.gifted_points = int(gifted_points)
        self.percent_to_next = float(percent_to_next)
        self.spent_points = int(spent_points)

class DailyRibbon:

    def __init__(self, count: str, date: str, time: str):
        self.count = int(count)
        self.date = arrow.get(date)
        self.time = arrow.get(time)


class CharacterName:

    def __init__(self, first: str, first_lower:str):
        self.first = first
        self.first_lower = first_lower


class OutfitMember:

    def __init__(self, 
        battle_rank: BattleRank,
        certs: CertificationPoints,
        character_id: str,
        character_id_merged: str,
        daily_ribbon: DailyRibbon,
        faction_id: str,
        head_id: str,
        member_since: str,
        member_since_date: str,
        member_since_date_merged: str,
        name: CharacterName,
        online_status: str,
        profile_id: str):

        self.battle_rank = battle_rank
        self.certs = certs
        self.character_id = character_id
        self.character_id_merged = character_id_merged
        self.daily_ribbon = daily_ribbon
        self.faction_id = faction_id
        self.head_id = head_id
        self.member_since = arrow.get(member_since)
        self.member_since_date = arrow.get(member_since_date)
        self.member_since_date_merged = arrow.get(member_since_date_merged)
        self.name = name
        self.online_status = bool(int(online_status))
        self.profile_id = profile_id

class Outfit:

    def __init__(self, 
        alias:str,
        alias_lower:str,
        name:str,
        name_lower: str,
        time_created:str,
        time_created_date:str,
        leader_character_id:str,
        outfit_id:str,
        member_count:str,
        members: list):

        self.alias = alias
        self.alias_lower = alias_lower
        self.leader_character_id = leader_character_id
        self.member_count = int(member_count)
        self.time_created = arrow.get(time_created)
        self.time_created_date = arrow.get(time_created_date)
        self.name = name
        self.name_lower = name_lower
        self.outfit_id = outfit_id
        self.members = []
        for member in members:
            try:
                self.members.append(
                    OutfitMember(
                        battle_rank = BattleRank(**member['battle_rank'] or 1),
                        certs = CertificationPoints(**member['certs']),
                        daily_ribbon = DailyRibbon(**member['daily_ribbon']),
                        name = CharacterName(**member['name']),
                        character_id = member['character_id'],
                        character_id_merged = member['character_id_merged'],
                        faction_id = member['faction_id'],
                        head_id = member['head_id'],
                        member_since = member['member_since'],
                        member_since_date = member['member_since_date'],
                        member_since_date_merged = member['member_since_date_merged'],
                        online_status = member['online_status'],
                        profile_id = member['profile_id']
                        )
                )
            except KeyError:
                # discard invalid data
                pass

    def __repr__(self):
        return '''
            Outfit: {}
            Member count: {}
            Crreated: {} '''.format(self.name, self.member_count, self.time_created_date)

    
