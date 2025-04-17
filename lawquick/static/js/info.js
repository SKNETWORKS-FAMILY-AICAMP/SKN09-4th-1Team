function skipSection(input) {
  // .skip-btn → label → .info-title → .info-content (형제 관계)
  const label = input.closest('.skip-btn');
  if (!label) return;

  const infoTitle = label.closest('.info-title');
  if (!infoTitle) {
    console.error("info-title을 찾을 수 없습니다.");
    return;
  }

  const contentSection = infoTitle.parentElement.querySelector('.info-content');
  if (!contentSection) {
    console.error("info-content를 찾을 수 없습니다.");
    return;
  }

  if (input.checked) {
    contentSection.innerHTML = `<p style="color: gray;">이 섹션은 건너뛰셨습니다.</p>`;
    console.log(`[${input.name}] 섹션이 건너뛰기 처리되었습니다.`);
  } else {
    alert("입력 폼을 복원하려면 페이지를 새로고침 해주세요.");
    console.log(`[${input.name}] 섹션 건너뛰기 해제되었습니다.`);
  }
}
