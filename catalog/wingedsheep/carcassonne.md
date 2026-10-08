---
repository: "wingedsheep/carcassonne"
github_id: 264605327
url: "https://github.com/wingedsheep/carcassonne"
description: "Carcassonne implementation in python"
starred_at: "2022-12-02T20:43:03Z"
language: "Python"
topics: ["boardgame", "carcassonne"]
homepage: ""
license: "MIT"
archived: false
---

# wingedsheep/carcassonne

Carcassonne implementation in python

**GitHub:** https://github.com/wingedsheep/carcassonne

## README excerpt

> # carcassonne
> Carcassonne implementation in python
> ## Features
> * Tilesets
> * Base game
> * The river
> * Inns and cathedrals
> * Abbots
> * Farmers
> ## Installation
> * Clone the project
> * Go to the project folder
> * Run:
> pip install .
> You can now use the API in other projects.
> ## API
> Code example for a game with two players
> import random
> from typing import Optional
> from wingedsheep.carcassonne.carcassonne_game import CarcassonneGame
> from wingedsheep.carcassonne.carcassonne_game_state import CarcassonneGameState
> from wingedsheep.carcassonne.objects.actions.action import Action
> from wingedsheep.carcassonne.tile_sets.supplementary_rules import SupplementaryRule
> from wingedsheep.carcassonne.tile_sets.tile_sets import TileSet
> game = CarcassonneGame(
> players=2,
> tile_sets=[TileSet.BASE, TileSet.THE_RIVER, TileSet.INNS_AND_CATHEDRALS],
> supplementary_rules=[SupplementaryRule.ABBOTS, SupplementaryRule.FARMERS]
> )
> while not game.is_finished():
> player: int = game.get_current_player()
> valid_actions: [Action] = game.get_possible_actions()
> action: Optional[Action] = random.choice(valid_actions)
> if action is not None:
> game.step(player, action)
> game.render()

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

A Python implementation of the Carcassonne board game, providing an API for building game clients or simulations. It supports the base game, The River, Inns and Cathedrals tile sets, and the Abbots and Farmers supplementary rules.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "fc93829d168ccdaeb403d5ec7969016e7b9a243e61237140b90ca928d9a43d1a"
  },
  "primary_domain": "games",
  "secondary_domains": [
    "applications"
  ],
  "repository_type": "library",
  "capabilities": [
    "gameplay",
    "simulation"
  ],
  "technologies": [
    "Python"
  ],
  "summary": "A Python implementation of the Carcassonne board game, providing an API for building game clients or simulations. It supports the base game, The River, Inns and Cathedrals tile sets, and the Abbots and Farmers supplementary rules.",
  "use_cases": [
    "Simulating two-player Carcassonne games with random or scripted agents",
    "Building a Carcassonne front end or AI on top of the game API",
    "Experimenting with tile set and supplementary rule combinations"
  ],
  "limitations": [
    "Only the features listed in the README are documented; other rules or tile sets are not described",
    "README example uses random action selection and does not describe any strategy or AI"
  ],
  "suggested_terms": [
    "carcassonne",
    "board game python",
    "tile placement game",
    "game engine python",
    "boardgame api"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
