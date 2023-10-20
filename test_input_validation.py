import pytest
from input_validation import is_valid_email, is_valid_password


@pytest.mark.parametrize("email", [
    ("test@email.com")
,   ("t.est@email.com")
,   ("test@em.ail.com")
,   ("test@email.co.uk")
,   ("te-st@email.com")
,   ("te_st@email.com")
,   ("test1@email.com")
,   ("G.Karagkiaouridis@outlook.com")
,   ("georkara12@gmail.com")
,   ("seeeko66@gmail.com")
])
def test_is_valid_email__gueltige_Adressen(email):
    # arrange
    email_adress_to_be_tested = email
    
    # act
    response = is_valid_email(email)
    
    # assert
    assert response is True


@pytest.mark.parametrize("email", [
    ("testemail.com")   # Fehlendes @-Zeichen
,   ("test@email")      # Fehlende Top-Level-Domain
,   ("test@em@ail.com") # Mehrfaches @-Zeichen
])
def test_is_valid_email__ungueltige_Adressen(email):
    # arrange
    email_adress_to_be_tested = email
    
    # act
    response = is_valid_email(email)
    
    # assert
    assert response is False

@pytest.mark.parametrize("pwd", [
    ("HalloichheißeMarvinundbintoll")
,   ("Test123!"),("Friedeltest")
])

def test_is_valid_password(pwd):
    pwd_to_be_tested = pwd
    response = is_valid_password(pwd)
    assert response is True
