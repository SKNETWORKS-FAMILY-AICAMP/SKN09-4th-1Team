document.addEventListener("DOMContentLoaded", () => {
  const sidebarToggleBtn = document.querySelector(".hamburger-btn");
  const sidebar = document.getElementById("sidebar");
  const appWrapper = document.querySelector(".app-wrapper");
  const userIconBtn = document.getElementById("userIconBtn");
  const userDropdown = document.getElementById("userDropdown");

  sidebar?.addEventListener("click", (e) => e.stopPropagation());
  sidebarToggleBtn?.addEventListener("click", (e) => {
    sidebar.classList.toggle("active");
    appWrapper.classList.toggle("sidebar-open");
    e.stopPropagation();
  });

  userIconBtn?.addEventListener("click", (e) => {
    userDropdown.style.display =
      userDropdown.style.display === "flex" ? "none" : "flex";
    e.stopPropagation();
  });

  document.addEventListener("click", () => {
    userDropdown.style.display = "none";
    sidebar?.classList.remove("active");
    appWrapper?.classList.remove("sidebar-open");
  });
});

function handleTitleClick(event, chatId) {
  const input = document.querySelector(`#chat-title-${chatId}`);
  if (!input.hasAttribute("readonly")) {
    // 수정 중이면 이동 막기
    event.stopPropagation();
    return;
  }
  goToChat(chatId);
}

function editChatTitle(chatId) {
  const input = document.querySelector(`#chat-title-${chatId}`);
  input.removeAttribute("readonly");
  input.focus();

  input.addEventListener("mousedown", (e) => {
    e.stopPropagation();
  }, { once: true });

  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      saveChatTitle(chatId, input);
    }
  }, { once: true });

  input.addEventListener("blur", () => {
    saveChatTitle(chatId, input);
  }, { once: true });
}

function saveChatTitle(chatId, input) {
  const newTitle = input.value.trim();
  if (!newTitle) {
    alert("제목은 비워둘 수 없습니다.");
    input.focus();
    return;
  }

  fetch(`/chat/member/update-title/${chatId}/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCSRFToken(),
    },
    body: JSON.stringify({ title: newTitle }),
  }).then((res) => {
    if (res.ok) {
      input.setAttribute("readonly", true);
    } else {
      alert("제목 수정 실패");
    }
  }).catch((e) => {
    alert("서버 오류: " + e.message);
  });
}

function deleteChat(chatId) {
  if (!confirm("이 채팅을 삭제하시겠습니까?")) return;

  const currentPath = window.location.pathname;
  const isCurrentChat = currentPath.includes(`/member/chat/${chatId}/`);

  fetch(`/chat/member/delete/${chatId}/`, {
    method: "POST",
    headers: {
      "X-CSRFToken": getCSRFToken(),
    },
  }).then((res) => {
    if (res.ok) {
      document.querySelector(`#chat-${chatId}`)?.remove();

      if (isCurrentChat) {
        const firstRemainingChat = document.querySelector(".question-item");
        if (firstRemainingChat) {
          const firstInput = firstRemainingChat.querySelector("input");
          if (firstInput) {
            const id = firstInput.id.replace("chat-title-", "");
            goToChat(id);
          }
        } else {
          window.location.href = "/chat/member/00/";
        }
      }
    } else {
      alert("삭제 실패 😥");
    }
  });
}

function goToChat(chatId) {
  const form = document.createElement("form");
  form.method = "POST";
  form.action = `/chat/member/chat/${chatId}/`;

  const csrfToken = getCSRFToken();
  const csrfInput = document.createElement("input");
  csrfInput.type = "hidden";
  csrfInput.name = "csrfmiddlewaretoken";
  csrfInput.value = csrfToken;
  form.appendChild(csrfInput);

  document.body.appendChild(form);
  form.submit();
}

function getCSRFToken() {
  const name = 'csrftoken';
  const cookie = document.cookie
    .split(';')
    .find((c) => c.trim().startsWith(name + '='));
  return cookie ? cookie.trim().split('=')[1] : '';
}