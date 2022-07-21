from pydantic import Field
from pydantic.datetime_parse import datetime
from pydantic.types import UUID4, Dict, List, PastDate

from models.common_model import HabiticaBaseModel
from models.notification_model import Notification


class Auth(HabiticaBaseModel):
    #     "local":{
    #             "username":"second_test_api",
    #             "lowerCaseUsername":"second_test_api",
    #             "email":"alexandrettio+2@gmail.com",
    #             "has_password":true
    #          },
    #          "timestamps":{
    #             "created":"2022-07-11T08:21:17.391Z",
    #             "loggedin":"2022-07-15T08:08:04.384Z",
    #             "updated":"2022-07-18T11:53:01.066Z"
    #          },
    #          "facebook":{
    #
    #          },
    #          "google":{
    #
    #          },
    #          "apple":{
    #
    #          }
    pass


class Achievements(HabiticaBaseModel):
    pass
    # "achievements":{
    #    "ultimateGearSets":{
    #       "healer":false,
    #       "wizard":false,
    #       "rogue":false,
    #       "warrior":false
    #    },
    #    "streak":0,
    #    "challenges":[
    #
    #    ],
    #    "perfect":0,
    #    "quests":{
    #
    #    },
    #    "partyUp":true
    # },
    #


class Purchased(HabiticaBaseModel):
    pass
    # "purchased": {
    #     "ads": false,
    #     "txnCount": 0,
    #     "skin": {
    #
    #     },
    #     "hair": {
    #
    #     },
    #     "shirt": {
    #
    #     },
    #     "background": {
    #         "violet": true,
    #         "blue": true,
    #         "green": true,
    #         "purple": true,
    #         "red": true,
    #         "yellow": true
    #     },
    #     "plan": {
    #         "consecutive": {
    #             "count": 0,
    #             "offset": 0,
    #             "gemCapExtra": 0,
    #             "trinkets": 0
    #         },
    #         "quantity": 1,
    #         "extraMonths": 0,
    #         "gemsBought": 0,
    #         "mysteryItems": [
    #
    #         ],
    #         "dateUpdated": "2022-07-12T08:39:06.846Z"
    #     }
    # },


class Flags(HabiticaBaseModel):
    tour: Dict
    tutorial: Dict
    customizations_notification: bool
    show_tour: bool
    drops_enabled: bool
    items_enabled: bool
    rewrite: bool
    class_selected: bool
    rebirth_enabled: bool
    welcomed: bool
    armoire_enabled: bool
    armoire_opened: bool
    armoire_empty: bool
    card_received: bool
    warned_low_health: bool
    verified_username: bool
    new_stuff: bool
    community_guidelines_accepted: bool
    recapture_emails_phase: int
    weekly_recap_emails_phase: int
    cron_count: int
    level_drops: Dict
    last_weekly_recap: datetime


class History(HabiticaBaseModel):
    exp: List  # Todo: List of events?
    todos: List


class Items(HabiticaBaseModel):
    pass
    # "items":{
    #          "gear":{
    #             "equipped":{
    #                "armor":"armor_base_0",
    #                "head":"head_base_0",
    #                "shield":"shield_base_0"
    #             },
    #             "costume":{
    #                "armor":"armor_base_0",
    #                "head":"head_base_0",
    #                "shield":"shield_base_0"
    #             },
    #             "owned":{
    #                "headAccessory_special_blackHeadband":true,
    #                "headAccessory_special_blueHeadband":true,
    #                "headAccessory_special_greenHeadband":true,
    #                "headAccessory_special_pinkHeadband":true,
    #                "headAccessory_special_redHeadband":true,
    #                "headAccessory_special_whiteHeadband":true,
    #                "headAccessory_special_yellowHeadband":true,
    #                "eyewear_special_blackTopFrame":true,
    #                "eyewear_special_blueTopFrame":true,
    #                "eyewear_special_greenTopFrame":true,
    #                "eyewear_special_pinkTopFrame":true,
    #                "eyewear_special_redTopFrame":true,
    #                "eyewear_special_whiteTopFrame":true,
    #                "eyewear_special_yellowTopFrame":true,
    #                "eyewear_special_blackHalfMoon":true,
    #                "eyewear_special_blueHalfMoon":true,
    #                "eyewear_special_greenHalfMoon":true,
    #                "eyewear_special_pinkHalfMoon":true,
    #                "eyewear_special_redHalfMoon":true,
    #                "eyewear_special_whiteHalfMoon":true,
    #                "eyewear_special_yellowHalfMoon":true,
    #                "armor_special_bardRobes":true,
    #                "head_special_bardHat":true
    #             }
    #          },
    #          "special":{
    #             "snowball":0,
    #             "spookySparkles":0,
    #             "shinySeed":0,
    #             "seafoam":0,
    #             "valentine":0,
    #             "valentineReceived":[
    #
    #             ],
    #             "nye":0,
    #             "nyeReceived":[
    #
    #             ],
    #             "greeting":0,
    #             "greetingReceived":[
    #
    #             ],
    #             "thankyou":0,
    #             "thankyouReceived":[
    #
    #             ],
    #             "birthday":0,
    #             "birthdayReceived":[
    #
    #             ],
    #             "congrats":0,
    #             "congratsReceived":[
    #
    #             ],
    #             "getwell":0,
    #             "getwellReceived":[
    #
    #             ],
    #             "goodluck":0,
    #             "goodluckReceived":[
    #
    #             ]
    #          },
    #          "lastDrop":{
    #             "count":0,
    #             "date":"2022-07-11T08:21:17.394Z"
    #          },
    #          "pets":{
    #
    #          },
    #          "eggs":{
    #
    #          },
    #          "hatchingPotions":{
    #             "RoyalPurple":1
    #          },
    #          "food":{
    #
    #          },
    #          "mounts":{
    #             "Orca-Base":true
    #          },
    #          "quests":{
    #             "dustbunnies":1,
    #             "basilist":370
    #          }
    #       },


class Invitations(HabiticaBaseModel):
    guilds: List
    party: Dict
    parties: List


class Party(HabiticaBaseModel):
    pass
    # "party":{
    #          "quest":{
    #             "progress":{
    #                "up":0,
    #                "down":0,
    #                "collectedItems":0,
    #                "collect":{
    #
    #                }
    #             },
    #             "RSVPNeeded":true,
    #             "key":"basilist",
    #             "completed":"None"
    #          },
    #          "order":"level",
    #          "orderAscending":"ascending",
    #          "_id":"db8061d1-bccc-4f79-8a72-c00d7cc801d7"
    #       },


class Preferences(HabiticaBaseModel):
    pass
    # "preferences":{
    #          "hair":{
    #             "color":"red",
    #             "base":3,
    #             "bangs":1,
    #             "beard":0,
    #             "mustache":0,
    #             "flower":1
    #          },
    #          "emailNotifications":{
    #             "unsubscribeFromAll":false,
    #             "newPM":true,
    #             "kickedGroup":true,
    #             "wonChallenge":true,
    #             "giftedGems":true,
    #             "giftedSubscription":true,
    #             "invitedParty":true,
    #             "invitedGuild":true,
    #             "questStarted":true,
    #             "invitedQuest":true,
    #             "importantAnnouncements":true,
    #             "weeklyRecaps":true,
    #             "onboarding":true,
    #             "majorUpdates":true,
    #             "subscriptionReminders":true
    #          },
    #          "pushNotifications":{
    #             "unsubscribeFromAll":false,
    #             "newPM":true,
    #             "wonChallenge":true,
    #             "giftedGems":true,
    #             "giftedSubscription":true,
    #             "invitedParty":true,
    #             "invitedGuild":true,
    #             "questStarted":true,
    #             "invitedQuest":true,
    #             "majorUpdates":true,
    #             "mentionParty":true,
    #             "mentionJoinedGuild":true,
    #             "mentionUnjoinedGuild":true,
    #             "partyActivity":true
    #          },
    #          "suppressModals":{
    #             "levelUp":false,
    #             "hatchPet":false,
    #             "raisePet":false,
    #             "streak":false
    #          },
    #          "tasks":{
    #             "groupByChallenge":false,
    #             "confirmScoreNotes":false
    #          },
    #          "dayStart":0,
    #          "size":"slim",
    #          "hideHeader":false,
    #          "skin":"915533",
    #          "shirt":"blue",
    #          "timezoneOffset":-180,
    #          "sound":"rosstavoTheme",
    #          "chair":"none",
    #          "allocationMode":"flat",
    #          "autoEquip":true,
    #          "dateFormat":"MM/dd/yyyy",
    #          "sleep":false,
    #          "stickyHeader":true,
    #          "disableClasses":false,
    #          "newTaskEdit":false,
    #          "dailyDueDefaultView":false,
    #          "advancedCollapsed":false,
    #          "toolbarCollapsed":false,
    #          "reverseChatOrder":false,
    #          "displayInviteToPartyWhenPartyIs1":true,
    #          "improvementCategories":[
    #
    #          ],
    #          "language":"en",
    #          "webhooks":{
    #
    #          },
    #          "background":"violet",
    #          "timezoneOffsetAtLastCron":-180
    #       },


class Profile(HabiticaBaseModel):
    name: str


class Stats(HabiticaBaseModel):
    buffs: Dict  # TODO class
    training: Dict  # TODO class
    hp: float
    mp: float
    exp: float
    gp: float
    lvl: float
    points: float
    strength: float = Field(alias="str")
    constitution: float = Field(alias="con")
    intelligence: float = Field(alias="int")
    perception: float = Field(alias="per")
    to_next_level: float
    max_health: float
    max_MP: float
    user_class: str = Field(alias="class")  # TODO enum

    #          "buffs":{
    #             "str":0,
    #             "int":0,
    #             "per":0,
    #             "con":0,
    #             "stealth":0,
    #             "streaks":false,
    #             "snowball":false,
    #             "spookySparkles":false,
    #             "shinySeed":false,
    #             "seafoam":false
    #          },
    #          "training":{
    #             "int":0,
    #             "per":0,
    #             "str":0,
    #             "con":0
    #          },
    #       },


class Inbox(HabiticaBaseModel):
    newMessages: int
    optOut: bool
    blocks: List
    messages: Dict


class TasksOrder(HabiticaBaseModel):
    habits: List
    dailys: List
    todos: List
    rewards: List


class Item(HabiticaBaseModel):
    type: str  # TODO maybe enum
    path: str


class Tag(HabiticaBaseModel):
    name: str
    id: UUID4


class NewMessage(HabiticaBaseModel):
    pass
    # "db8061d1-bccc-4f79-8a72-c00d7cc801d7":{
    #             "name":"second_test_api's Party",
    #             "value":true
    #          }


class User(HabiticaBaseModel):
    auth: Auth
    achievements: Achievements
    backer: Dict
    contributor: Dict
    permissions: Dict
    purchased: Purchased
    flags: Flags
    history: History
    items: Items
    invitations: Invitations
    party: Party
    preferences: Preferences
    profile: Profile
    stats: Stats
    inbox: Inbox
    tasksOrder: TasksOrder
    balance: int
    challenges: List
    guilds: List
    loginIncentives: int
    invitesSent: int
    pinnedItemsOrder: List
    secret_id: UUID4 = Field(alias="_id")
    lastCron: PastDate
    newMessages: Dict[NewMessage]
    notifications: List[Notification]
    tags: List[Tag]
    extra: Dict
    pushDevices: List
    webhooks: List
    pinnedItems: List[Item]
    unpinnedItems: List
    migration: str
    id: UUID4
    needsCron: bool
