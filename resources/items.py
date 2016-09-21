# /usr/bin/env python
# -*- coding: utf-8 -*-
import resources.common as common
from universal import lazy_property
import resources.utility as utility


class ItemResource(utility.CacheablePropertyResource):

    yaml_tag = '!ItemResource'

    class Meta:
        name = "Item"
        resource_name = "item"
        cache_folder = 'items/items/'
        identifier = 'id'
        attributes = (
            'id',
            'name',
            'cost',
            'fling_power',
            'fling_effect',
            'attributes',
            'category',
            'effect_entries',
            'flavor_text_entries',
            'game_indices',
            'names',
            'sprites',
            'held_by_pokemon',
            'baby_trigger_for',
            'machines'
        )

    @lazy_property
    def fling_effect(self):
        return common.NamedAPIResource(**self._fling_effect)

    @lazy_property
    def attributes(self):
        return [common.NamedAPIResource(**kwargs)
                for kwargs in self._attributes]

    @lazy_property
    def category(self):
        return common.NamedAPIResource(**self._category)

    @lazy_property
    def effect_entries(self):
        return [common.VerboseEffect(**kwargs)
                for kwargs in self._effect_entries]

    @lazy_property
    def flavor_text_entries(self):
        return [common.VersionGroupFlavorText(**kwargs)
                for kwargs in self._flavor_text_entries]

    @lazy_property
    def game_indicies(self):
        return [common.GenerationGameIndex(**kwargs) 
                for kwargs in self._game_indices]

    @lazy_property
    def names(self):
        return [common.Name(**kwargs) for kwargs in self._names]

    @lazy_property
    def sprites(self):
        return ItemSprites(**self._sprites)

    @lazy_property
    def held_by_pokemon(self):
        return [ItemHolderPokemon(**kwargs) for kwargs in self._held_by_pokemon]

    @lazy_property
    def baby_trigger_for(self):
        return common.APIResource(**self._baby_trigger_for)

    @lazy_property
    def machines(self):
        return [utility.MachineVersionDetail(**kwargs) 
                for kwargs in self._machines]


class ItemSprites:

    def __init__(self, **kwargs):
        self.default = kwargs['default']


class ItemHolderPokemon:

    def __init__(self, **kwargs):
        self.pokemon = kwargs['pokemon']
        self.version_details = ItemHolderPokemonVersionDetail(
            **kwargs['version_details'])


class ItemHolderPokemonVersionDetail:

    def __init__(self, **kwargs):
        self.rarity = kwargs['rarity']
        self.version = common.NamedAPIResource(**kwargs['version'])


class ItemAttributeResource(utility.CacheablePropertyResource):

    yaml_tag = '!ItemAttributeResource'

    class Meta:
        name = "Item Attribute"
        resource_name = "item-attribute"
        cache_folder = 'items/item-attributes/'
        identifier = 'id'
        attributes = (
            'id',
            'name',
            'items',
            'names',
            'descriptions'
        )


    @lazy_property
    def