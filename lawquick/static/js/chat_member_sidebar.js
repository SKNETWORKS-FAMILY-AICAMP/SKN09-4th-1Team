document.addEventListener("DOMContentLoaded", () => {
  const sidebarToggleBtn = document.querySelector(".chat-sidebar-btn");
  const sidebar = document.getElementById("sidebar");
  const appWrapper = document.querySelector(".app-wrapper");
  const userIconBtn = document.querySelector(".chat-user-icon");
  const userDropdown = document.querySelector(".chat-dropdown-menu");

  // 사이드바 열고 닫기
  sidebarToggleBtn?.addEventListener("click", (e) => {
    sidebar.classList.toggle("active");
    document.body.classList.toggle("sidebar-open");
    e.stopPropagation();
  });

  // 사용자 드롭다운 토글
  userIconBtn?.addEventListener("click", (e) => {
    userDropdown.classList.toggle("show");
    e.stopPropagation();
  });

  // 외부 클릭 시 드롭다운 닫기
  document.addEventListener("click", () => {
    userDropdown?.classList.remove("show");
  });

  // 사이드바 내부 클릭 이벤트 전파 방지
  sidebar?.addEventListener("click", (e) => e.stopPropagation());
});

// 채팅 제목 클릭 → 해당 채팅으로 이동
function handleTitleClick(event, chatId) {
  const input = document.querySelector(`#chat-title-${chatId}`);
  if (!input.hasAttribute("readonly")) {
    event.stopPropagation();
    return;
  }

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

// 제목 수정 시작
function editChatTitle(chatId) {
  const input = document.querySelector(`#chat-title-${chatId}`);
  input.removeAttribute("readonly");
  input.focus();

  // 수정 중 클릭 막기
  input.addEventListener("mousedown", (e) => e.stopPropagation(), { once: true });

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

// 제목 수정 저장 요청
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

// 채팅 삭제
function deleteChat(chatId) {
  if (!confirm("이 채팅을 삭제하시겠습니까?")) return;

  fetch(`/chat/member/delete/${chatId}/`, {
    method: "POST",
    headers: {
      "X-CSRFToken": getCSRFToken(),
    },
  }).then((res) => {
    if (res.ok) {
      document.querySelector(`#chat-${chatId}`)?.remove();
      window.location.href = "/chat/main/";
    } else {
      alert("삭제 실패");
    }
  });
}

// CSRF 토큰 가져오기
function getCSRFToken() {
  const name = "csrftoken";
  const cookie = document.cookie.split(";").find((c) => c.trim().startsWith(name + "="));
  return cookie ? cookie.trim().split("=")[1] : "";
}
