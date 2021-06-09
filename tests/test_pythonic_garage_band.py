from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import *
import pytest

def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def prep_data():
    suhaib =Guitarist("suhaib")
    ahmad = Drummer("ahmad")
    
    
    return {'suhaib':suhaib,'ahmad':ahmad}
def test_repr(prep_data):
    expected = 'guiter: suhaib'
    actual = prep_data['suhaib'].__repr__()
    assert actual == expected

def test_str(prep_data):
    expected='i am suhaib the guitar guy'
    actual = prep_data['suhaib'].__str__()
    assert expected == actual

def test_get_instrument(prep_data):
    acutal = prep_data['suhaib'].get_instrument()
    expected = 'Guitar'
    assert expected==acutal

def test_play_solo(prep_data):
    actual = prep_data['ahmad'].play_solo()
    expected = 'dom dom dom'
    assert expected ==actual

































# @pytest.mark.skip("todo")
# def test_guitarist_str():
#     suhaib = Guitarist("suhaib")
#     actual = str(suhaib)
#     expected = "My name is suhaib and I play guitar"
#     assert actual == expected


# # @pytest.mark.skip("todo")
# def test_guitarist_repr():
#     suhaib = Guitarist("suhaib")
#     actual = repr(suhaib)
#     expected = "Guitarist instance. Name = suhaib"
#     assert actual == expected


# # @pytest.mark.skip("todo")
# def test_drummer_str():
#     ahmad = Drummer("ahmad")
#     actual = str(ahmad)
#     expected = "My name is ahmad and I play drums"
#     assert actual == expected


# # @pytest.mark.skip("todo")
# def test_drummer_repr():
#     ahmad = Drummer("ahmad")
#     actual = repr(ahmad)
#     expected = "Drummer instance. Name = ahmad"
#     assert actual == expected


# # @pytest.mark.skip("todo")
# def test_bassist_str():
#     emad = Bassist("emad")
#     actual = str(emad)
#     expected = "My name is emad and I play bass"
#     assert actual == expected


# @pytest.mark.skip("todo")
# def test_bassist_repr():
#     emad = Bassist("emad")
#     actual = repr(emad)
#     expected = "Bassist instance. Name = emad"
#     assert actual == expected


# @pytest.mark.skip("todo")
# def test_band_name():
#     nirvana = Band("the family band", [])

#     assert nirvana.name == "the family band"


# @pytest.mark.skip("todo")
# def test_guitarist():
#     jimi = Guitarist("Jimi Hendrix")
#     assert jimi.name == "Jimi Hendrix"
#     assert jimi.get_instrument() == "guitar"


# @pytest.mark.skip("todo")
# def test_bassist():
#     flea = Bassist("Flea")
#     assert flea.name == "Flea"
#     assert flea.get_instrument() == "bass"


# @pytest.mark.skip("todo")
# def test_drummer():
#     ginger = Drummer("Ginger Baker")
#     assert ginger.name == "Ginger Baker"
#     assert ginger.get_instrument() == "drums"


# @pytest.mark.skip("todo")
# def test_instruments(one_band):
#     instruments = ["guitar", "bass", "drums"]
#     for i, member in enumerate(one_band.members):
#         # NOTE: see stretch goal where zip used
#         assert member.get_instrument() == instruments[i]


# @pytest.mark.skip("todo")
# def test_individual_solos(one_band):
#     for member in one_band.members:
#         if member.get_instrument() == "guitar":
#             assert member.play_solo() == "face melting guitar solo"
#         elif member.get_instrument() == "bass":
#             assert member.play_solo() == "bom bom buh bom"
#         elif member.get_instrument() == "drums":
#             assert member.play_solo() == "rattle boom crash"


# @pytest.mark.skip("todo")
# def test_band_members(one_band):

#     assert len(one_band.members) == 3

#     assert isinstance(one_band.members[0], Musician)
#     assert isinstance(one_band.members[0], Guitarist)
#     assert one_band.members[0].name == "Kurt Cobain"

#     assert isinstance(one_band.members[1], Musician)
#     assert isinstance(one_band.members[1], Bassist)
#     assert one_band.members[1].name == "Krist Novoselic"

#     assert isinstance(one_band.members[2], Musician)
#     assert isinstance(one_band.members[2], Drummer)
#     assert one_band.members[2].name == "Dave Grohl"


# @pytest.mark.skip("todo")
# def test_play_solos_for_whole_band(one_band):
#     solos = one_band.play_solos()
#     assert len(solos) == 3
#     assert solos[0] == "face melting guitar solo"
#     assert solos[1] == "bom bom buh bom"
#     assert solos[2] == "rattle boom crash"


# @pytest.mark.skip("todo")
# def test_class_tracks_instances():
#     assert Band.to_list() == []
#     the_nobodies = Band("The Nobodies", [])
#     assert len(Band.instances) == 1
#     assert Band.instances[0] == the_nobodies


# @pytest.mark.skip("todo")
# def test_to_list():
#     assert Band.to_list() == []
#     the_nobodies = Band("The Nobodies", [])
#     all_bands = Band.to_list()
#     assert len(all_bands) == 1
#     assert all_bands[0] == the_nobodies


# #######################
# # Fixtures
# #######################


# @pytest.fixture
# def nirvana_data():
#     return {
#         "name": "Nirvana",
#         "members": [
#             {"name": "Kurt Cobain", "instrument": "Guitar"},
#             {"name": "Krist Novoselic", "instrument": "Bass"},
#             {"name": "Dave Grohl", "instrument": "Drums"},
#         ],
#     }


# @pytest.fixture
# def one_band():
#     members = [
#         Guitarist("Kurt Cobain"),
#         Bassist("Krist Novoselic"),
#         Drummer("Dave Grohl"),
#     ]

#     some_band = Band("Nirvana", members)

#     return some_band


# @pytest.fixture(autouse=True)
# def clean():
#     """runs before each test automatically.
#     This is necessary because otherwise band instances added in one test
#     will bleed over to other tests
#     There's also a more advanced way to run code after each test as well
#     Check the docs for that. Hint: it uses yield
#     """
#     Band.instances = []

