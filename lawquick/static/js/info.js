// static/js/info-form.js
function skipSection(name) {
    const section = document.getElementsByName(name)[0].closest('.info-content');
    
    // 건너뛴 상태에서 다시 누르면 해제 되게 해야함
    console.log(`name: ${name} 건너뜀`);
    if (section) {
      section.innerHTML = '<p style="color: gray;">이 섹션은 건너뛰셨습니다.</p>';
    }
    
  }
  