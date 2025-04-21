# import pytest
# from django.urls import reverse
# from user.models import User

# @pytest.mark.django_db
# def test_chat_entry_guest_redirect(client):
#     session = client.session
#     session['guest'] = True
#     session.save()

#     response = client.get(reverse('chat:chat_entry'), follow=False)
#     assert response.status_code == 302
#     assert response.url == reverse('chat:main')


# @pytest.mark.django_db
# def test_chat_entry_member_redirect(client):
#     user = User.objects.create(email="user@example.com", password="pw")
#     session = client.session
#     session['user_id'] = str(user.id)
#     session.save()

#     response = client.get(reverse('chat:chat_entry'), follow=False)
#     assert response.status_code == 302
#     assert response.url == reverse('chat:main')


# @pytest.mark.django_db
# def test_chat_entry_unauthenticated_redirect(client):
#     response = client.get(reverse('chat:chat_entry'), follow=False)
#     assert response.status_code == 302
#     assert response.url == reverse('user:home')

# import pytest
# from django.urls import reverse
# from user.models import User

# @pytest.mark.django_db
# def test_chat_entry_guest_redirect(client):
#     session = client.session
#     session['guest'] = True
#     session.save()

#     response = client.get(reverse('chat:chat_entry'), follow=True)
#     assert response.status_code == 200
#     # assert response.url == reverse('chat:main')
#     assert "어떤 점이 고민이신가요?" in response.content.decode("utf-8")



# @pytest.mark.django_db
# def test_chat_entry_member_redirect(client):
#     user = User.objects.create(email="user@example.com", password="pw")
#     session = client.session
#     session['user_id'] = str(user.id)
#     session.save()

#     response = client.get(reverse('chat:chat_entry'), follow=False)
#     assert response.status_code == 302
#     assert response.url == reverse('chat:main')


# @pytest.mark.django_db
# def test_chat_entry_unauthenticated_redirect(client):
#     response = client.get(reverse('chat:chat_entry'), follow=False)
#     assert response.status_code == 302
#     assert response.url == reverse('user:home')
import pytest
import uuid
from django.urls import reverse
from user.models import User

@pytest.mark.django_db
def test_chat_entry_guest_redirect(client):
    session = client.session
    session['guest'] = True  # Boolean True
    session['guest_user_id'] = str(uuid.uuid4())  # 실제 존재하지 않아도 무방
    session.save()

    response = client.get(reverse('chat:chat_entry'), follow=False)

    assert response.status_code == 302
    assert response.url == reverse('chat:main')


@pytest.mark.django_db
def test_chat_entry_member_redirect(client):
    user = User.objects.create(email="user@example.com", password="pw")
    session = client.session
    session['user_id'] = str(user.id)
    session['user_email'] = user.email
    session['guest'] = False
    session.save()

    response = client.get(reverse('chat:chat_entry'), follow=False)

    assert response.status_code == 302
    assert response.url == reverse('chat:main')


@pytest.mark.django_db
def test_chat_entry_unauthenticated_redirect(client):
    # 세션 없음
    response = client.get(reverse('chat:chat_entry'), follow=False)

    assert response.status_code == 302
    assert response.url == reverse('user:home')
