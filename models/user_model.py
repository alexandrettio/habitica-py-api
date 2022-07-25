from typing import Any, Dict, List

from pydantic import Field
from pydantic.datetime_parse import datetime
from pydantic.types import UUID4, PastDate

from consts import ClassType
from models.common_model import HabiticaBaseModel, Response
from models.notification_model import Notification
from models.tag_model import Tag


class Local(HabiticaBaseModel):
    username: str
    lower_case_username: str
    email: str
    has_password: bool


class Timestamps(HabiticaBaseModel):
    created: str
    logged_in: str
    updated: str


class Auth(HabiticaBaseModel):
    local: Local
    timestamps: Timestamps
    facebook: Dict[str, Any]
    google: Dict[str, Any]
    apple: Dict[str, Any]


class UltimateGearSets(HabiticaBaseModel):
    healer: bool
    wizard: bool
    rogue: bool
    warrior: bool


class Achievements(HabiticaBaseModel):
    ultimate_gear_sets: UltimateGearSets
    streak: int
    challenges: List
    perfect: int
    quests: Dict[str, Any]
    party_up: bool
    created_task: bool
    completed_task: bool
    purchased_equipment: bool


class Consecutive(HabiticaBaseModel):
    count: int
    offset: int
    gem_cap_extra: int
    trinkets: int


class Plan(HabiticaBaseModel):
    consecutive: Consecutive
    quantity: int
    extra_months: int
    gems_bought: int
    mystery_items: List
    date_updated: str


class Purchased(HabiticaBaseModel):
    ads: bool
    txn_count: int = Field(..., alias="txnCount")
    skin: Dict[str, Any]
    hair: Dict[str, Any]
    shirt: Dict[str, Any]
    background: Dict[str, Any]
    plan: Plan


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


class Equipped(HabiticaBaseModel):
    armor: str
    head: str
    shield: str
    weapon: str


class Costume(HabiticaBaseModel):
    armor: str
    head: str
    shield: str


class Owned(HabiticaBaseModel):
    head_accessory_special_black_headband: bool
    head_accessory_special_blue_headband: bool
    head_accessory_special_green_headband: bool
    head_accessory_special_pink_headband: bool
    head_accessory_special_red_headband: bool
    head_accessory_special_white_headband: bool
    head_accessory_special_yellow_headband: bool
    eyewear_special_black_top_frame: bool
    eyewear_special_blue_top_frame: bool
    eyewear_special_green_top_frame: bool
    eyewear_special_pink_top_frame: bool
    eyewear_special_red_top_frame: bool
    eyewear_special_white_top_frame: bool
    eyewear_special_yellow_top_frame: bool
    eyewear_special_black_half_moon: bool
    eyewear_special_blue_half_moon: bool
    eyewear_special_green_half_moon: bool
    eyewear_special_pink_half_moon: bool
    eyewear_special_red_half_moon: bool
    eyewear_special_white_half_moon: bool
    eyewear_special_yellow_half_moon: bool
    armor_special_bard_robes: bool
    head_special_bard_hat: bool
    weapon_warrior_0: bool
    armor_warrior_1: bool


class Gear(HabiticaBaseModel):
    equipped: Equipped
    costume: Costume
    owned: Owned


class Special(HabiticaBaseModel):
    snowball: int
    spooky_sparkles: int
    shiny_seed: int
    seafoam: int
    valentine: int
    valentine_received: List
    nye: int
    nye_received: List
    greeting: int
    greeting_received: List
    thankyou: int
    thankyou_received: List
    birthday: int
    birthday_received: List
    congrats: int
    congrats_received: List
    get_well: int
    get_well_received: List
    good_luck: int
    good_luck_received: List


class LastDrop(HabiticaBaseModel):
    count: int
    date: str


class Eggs(HabiticaBaseModel):
    # TODO What to do with new eggs
    fox: int


class HatchingPotions(HabiticaBaseModel):
    # TODO What to do with new potions
    royal_purple: int
    white: int
    zombie: int


class Food(HabiticaBaseModel):
    chocolate: int
    meat: int
    cotton_candy_pink: int
    cotton_candy_blue: int
    rotten_meat: int


class Items(HabiticaBaseModel):
    gear: Gear
    special: Special
    last_drop: LastDrop
    pets: Dict[str, Any]
    eggs: Eggs
    hatching_potions: HatchingPotions
    food: Food
    mounts: Dict[str, Any]
    quests: Dict[str, Any]


class Invitations(HabiticaBaseModel):
    guilds: List
    party: Dict[str, Any]
    parties: List


class Progress(HabiticaBaseModel):
    up: int
    down: int
    collected_items: int
    collect: Dict[str, Any]


class Quest(HabiticaBaseModel):
    progress: Progress
    rsvp_needed: bool


class Party(HabiticaBaseModel):
    quest: Quest
    order: str
    order_ascending: str


class Hair(HabiticaBaseModel):
    color: str
    base: int
    bangs: int
    beard: int
    mustache: int
    flower: int


class EmailNotificationsPreferences(HabiticaBaseModel):
    unsubscribe_from_all: bool
    new_pm: bool
    kicked_group: bool
    won_challenge: bool
    gifted_gems: bool
    gifted_subscription: bool
    invited_party: bool
    invited_guild: bool
    quest_started: bool
    invited_quest: bool
    important_announcements: bool
    weekly_recaps: bool
    onboarding: bool
    major_updates: bool
    subscription_reminders: bool


class PushNotificationsPreferences(HabiticaBaseModel):
    unsubscribe_from_all: bool
    new_pm: bool
    won_challenge: bool
    gifted_gems: bool
    gifted_subscription: bool
    invited_party: bool
    invited_guild: bool
    quest_started: bool
    invited_quest: bool
    major_updates: bool
    mention_party: bool
    mention_joined_guild: bool
    mention_unjoined_guild: bool
    party_activity: bool


class SuppressModalsPreferences(HabiticaBaseModel):
    level_up: bool
    hatch_pet: bool
    raise_pet: bool
    streak: bool


class TaskPreferences(HabiticaBaseModel):
    group_by_challenge: bool
    confirm_score_notes: bool


class Preferences(HabiticaBaseModel):
    hair: Hair
    email_notifications: EmailNotificationsPreferences
    push_notifications: PushNotificationsPreferences
    suppress_modals: SuppressModalsPreferences
    tasks: TaskPreferences
    day_start: int
    size: str
    hide_header: bool
    skin: str
    shirt: str
    timezone_offset: int
    sound: str
    chair: str
    allocation_mode: str
    auto_equip: bool
    date_format: str
    sleep: bool
    sticky_header: bool
    disable_classes: bool
    new_task_edit: bool
    daily_due_default_view: bool
    advanced_collapsed: bool
    toolbar_collapsed: bool
    reverse_chat_order: bool
    display_invite_to_party_when_party_is1: bool
    improvement_categories: List
    language: str
    webhooks: Dict[str, Any]
    background: str
    timezone_offset_at_last_cron: int


class Profile(HabiticaBaseModel):
    name: str


class Buffs(HabiticaBaseModel):
    strength: float = Field(alias="str")
    constitution: float = Field(alias="con")
    intelligence: float = Field(alias="int")
    perception: float = Field(alias="per")
    stealth: int
    streaks: bool
    snowball: bool
    spooky_sparkles: bool
    shiny_seed: bool
    seafoam: bool


class Training(HabiticaBaseModel):
    strength: float = Field(alias="str")
    constitution: float = Field(alias="con")
    intelligence: float = Field(alias="int")
    perception: float = Field(alias="per")


class Stats(HabiticaBaseModel):
    buffs: Buffs
    training: Training
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
    user_class: ClassType = Field(alias="class")


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


class SleepWakeUpResponse(Response):
    data: bool


class UserInfo(HabiticaBaseModel):
    auth: Auth
    achievements: Achievements
    backer: Dict[str, Any]
    contributor: Dict[str, Any]
    permissions: Dict[str, Any]
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
    tasks_order: TasksOrder
    # _v: int
    balance: int
    challenges: List
    guilds: List
    login_incentives: int
    invites_sent: int
    pinned_items_order: List
    secret_id: UUID4 = Field(alias="_id")
    last_cron: PastDate
    new_messages: Dict[str, Any]
    notifications: List[Notification]
    tags: List[Tag]
    extra: Dict[str, Any]
    push_devices: List
    webhooks: List
    pinned_items: List[Item]
    unpinned_items: List
    migration: str
    id: UUID4
    needs_cron: bool


class GetUserInfoResponse(Response):
    data: UserInfo
