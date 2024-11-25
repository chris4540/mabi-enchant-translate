CREATE TABLE "Enchant" (
    "id" INTEGER NOT NULL PRIMARY KEY,   -- Unique identifier for each scroll
    "name" NVARCHAR(160) NOT NULL,       -- Name of the scroll in English
    "rank" INT NOT NULL,                 -- Rank of the scroll, represented as negative integers
    "rank_name" NVARCHAR(4) NOT NULL,
    "maximum_damage" INTEGER,
    "minimum_damage" INTEGER,
    "strength" INTEGER,
    "dexterity" INTEGER,
    "intelligence" INTEGER,
    "effect" TEXT NOT NULL,      -- Effect of the scroll in plain text in English
    ------------------------------   LOCALIZATION  -------------------------------------------
    "name_zhtw"   TEXT NOT NULL,    -- Name of the scroll in Traditional Chinese
    "effect_zhtw" TEXT NOT NULL     -- Effect of the scroll in plain text in Traditional Chinese
)
