from enum import Enum


class EntityType(str, Enum):
    PRODUCTS = "products"
    CHORES = "chores"
    PRODUCT_BARCODES = "product_barcodes"
    BATTERIES = "batteries"
    LOCATIONS = "locations"
    QUANTITY_UNITS = "quantity_units"
    QUANTITY_UNIT_CONVERSIONS = "quantity_unit_conversions"
    SHOPPING_LIST = "shopping_list"
    SHOPPING_LISTS = "shopping_lists"
    SHOPPING_LOCATIONS = "shopping_locations"
    RECIPES = "recipes"
    RECIPES_POS = "recipes_pos"
    RECIPES_NESTINGS = "recipes_nestings"
    TASKS = "tasks"
    TASK_CATEGORIES = "task_categories"
    PRODUCT_GROUPS = "product_groups"
    EQUIPMENT = "equipment"
    USER_FIELDS = "userfields"
    USER_ENTITIES = "userentities"
    USER_OBJECTS = "userobjects"
    MEAL_PLAN = "meal_plan"
    MEAL_PLAN_SECTIONS = "meal_plan_sections"

    def __str__(self):
        return self.value
