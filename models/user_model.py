from pydantic import BaseModel, Field
from pydantic.types import UUID4, Dict, List, PastDate

from models.notification_model import Notification


class Auth(BaseModel):
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


class Achievements(BaseModel):
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


class Purchased(BaseModel):
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


class Flags(BaseModel):
    pass
    # "flags": {
    #     "tour": {
    #         "intro": -2,
    #         "classes": -1,
    #         "stats": -1,
    #         "tavern": -1,
    #         "party": -2,
    #         "guilds": -1,
    #         "challenges": -1,
    #         "market": -1,
    #         "pets": -1,
    #         "mounts": -1,
    #         "hall": -1,
    #         "equipment": -1
    #     },
    #     "tutorial": {
    #         "common": {
    #             "habits": true,
    #             "dailies": true,
    #             "todos": true,
    #             "rewards": true,
    #             "party": true,
    #             "pets": true,
    #             "gems": true,
    #             "skills": true,
    #             "classes": true,
    #             "tavern": true,
    #             "equipment": true,
    #             "items": true,
    #             "mounts": true,
    #             "inbox": true,
    #             "stats": true
    #         },
    #         "ios": {
    #             "addTask": false,
    #             "editTask": false,
    #             "deleteTask": false,
    #             "filterTask": false,
    #             "groupPets": false,
    #             "inviteParty": false,
    #             "reorderTask": false
    #         }
    #     },
    #     "customizationsNotification": false,
    #     "showTour": true,
    #     "dropsEnabled": false,
    #     "itemsEnabled": false,
    #     "lastNewStuffRead": "04fc5964-63c0-4cb8-a296-c5077d3ae851",
    #     "rewrite": true,
    #     "classSelected": false,
    #     "rebirthEnabled": false,
    #     "recaptureEmailsPhase": 0,
    #     "weeklyRecapEmailsPhase": 0,
    #     "communityGuidelinesAccepted": true,
    #     "cronCount": 4,
    #     "welcomed": true,
    #     "armoireEnabled": true,
    #     "armoireOpened": false,
    #     "armoireEmpty": false,
    #     "cardReceived": false,
    #     "warnedLowHealth": false,
    #     "verifiedUsername": true,
    #     "levelDrops": {
    #
    #     },
    #     "lastWeeklyRecap": "2022-07-11T08:21:17.394Z",
    #     "newStuff": false
    # },


class History(BaseModel):
    pass
    # "history": {
    #     "exp": [
    #         {
    #             "date": "2022-07-12T08:39:06.797Z",
    #             "value": 0
    #         },
    #         {
    #             "date": "2022-07-12T21:41:27.626Z",
    #             "value": 0
    #         },
    #         {
    #             "date": "2022-07-14T18:57:48.146Z",
    #             "value": 0
    #         },
    #         {
    #             "date": "2022-07-15T08:08:04.384Z",
    #             "value": 0
    #         }
    #     ],
    #     "todos": [
    #         {
    #             "date": "2022-07-12T08:39:06.797Z",
    #             "value": -1
    #         },
    #         {
    #             "date": "2022-07-12T21:41:27.626Z",
    #             "value": -2.025956704627065
    #         },
    #         {
    #             "date": "2022-07-14T18:57:48.146Z",
    #             "value": -3.0792442306676366
    #         },
    #         {
    #             "date": "2022-07-15T08:08:04.384Z",
    #             "value": -4.161348258391508
    #         }
    #     ]
    # },


class Items(BaseModel):
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


class Invitations(BaseModel):
    pass
    # "invitations":{
    #          "guilds":[
    #
    #          ],
    #          "party":{
    #
    #          },
    #          "parties":[
    #
    #          ]
    #       },


class Party:
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


class Preferences:
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


class Profile:
    name: str


class Stats:
    pass
    # "stats":{
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
    #          "hp":50,
    #          "mp":30,
    #          "exp":0,
    #          "gp":0,
    #          "lvl":1,
    #          "class":"warrior",
    #          "points":0,
    #          "str":0,
    #          "con":0,
    #          "int":0,
    #          "per":0,
    #          "toNextLevel":25,
    #          "maxHealth":50,
    #          "maxMP":30
    #       },


class Inbox:
    newMessages: int
    optOut: bool
    blocks: List
    messages: Dict


class TasksOrder:
    pass
    # "tasksOrder":{
    #          "habits":[
    #             "2140d3e0-e4ac-4056-a939-347b28806154",
    #             "5fd21e9c-8dae-4f44-8644-a291259d2ff9"
    #          ],
    #          "dailys":[
    #
    #          ],
    #          "todos":[
    #             "099248ac-8817-471b-87a3-d0c93da5395b"
    #          ],
    #          "rewards":[
    #             "39708546-31e0-4fba-9dbf-baecaec6a452"
    #          ]
    #       },


class Item:
    type: str  # TODO maybe enum
    path: str


class Tag:
    name: str
    id: UUID4


class NewMessage:
    pass
    # "db8061d1-bccc-4f79-8a72-c00d7cc801d7":{
    #             "name":"second_test_api's Party",
    #             "value":true
    #          }


class User(BaseModel):
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
