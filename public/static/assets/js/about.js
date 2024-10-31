const teamGrid = document.getElementById('team-grid');

// Team members
const teamMembersData = window.teamMembers;

// Function to render the team members dynamically
function renderTeamMembers() {
    teamMembersData.forEach(member => {
        const memberDiv = document.createElement('div');
        memberDiv.classList.add('team-member');
        memberDiv.setAttribute('data-member', member.id);

        memberDiv.innerHTML = `
      <div>
        <img src="${member.image}" alt="${member.name}">
        <h3><i class="ri-arrow-right-s-line"></i>
        ${member.name}</h3>
        <p>${member.role}</p>
      </div>
    `;

        memberDiv.addEventListener('click', () => {
            handleMemberClick(member.id);
        });

        teamGrid.appendChild(memberDiv);
    });
}

// Function to handle custom scroll with an offset
function scrollToWithOffset(element, offset) {
    const elementPosition = element.getBoundingClientRect().top + window.pageYOffset;
    const offsetPosition = elementPosition - offset;

    window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
    });
}

// Function to handle member click event and toggle details display
function handleMemberClick(memberId) {
    const currentMember = teamMembersData.find(member => member.id === memberId);
    const clickedMember = document.querySelector(`[data-member='${memberId}']`);
    const currentDetails = document.querySelector('.dynamic-details');

    // If the clicked member is already active, hide the details
    if (clickedMember.classList.contains('active')) {
        clickedMember.classList.remove('active');
        if (currentDetails) currentDetails.remove();
        teamGrid.classList.remove('blurred');

        // Scroll back to the clicked member
        clickedMember.scrollIntoView({ behavior: 'smooth' });
        return;
    }


    // Remove any previous details before showing new ones
    if (currentDetails) currentDetails.remove();

    const detailsDiv = document.createElement('div');
    detailsDiv.classList.add('dynamic-details');
    detailsDiv.innerHTML = `
    <div class="row">
        <div class="col-6"> 
            <h1>${currentMember.name} </h1>
            <h4>${currentMember.role}</h4>
        </div>
        <div class="team-member-info col-6">${currentMember.details}</div>
    </div>
    `;

    // Find the clicked member's position and which row it's in
    const members = Array.from(document.querySelectorAll('.team-member'));

    // Calculate the row number based on how many members per row (3 per row on large screens, 1 per row on small screens)
    const membersPerRow = window.innerWidth <= 768 ? 1 : window.innerWidth <= 992 ? 2 : 3;
    const memberIndex = members.indexOf(clickedMember);
    const rowStartIndex = Math.floor(memberIndex / membersPerRow) * membersPerRow;
    const rowEndIndex = rowStartIndex + membersPerRow - 1;

    // Insert the details div after the last member in the row
    const lastMemberInRow = members[Math.min(rowEndIndex, members.length - 1)];
    lastMemberInRow.insertAdjacentElement('afterend', detailsDiv);

    // Blur the rest of the team members except the clicked one
    document.querySelectorAll('.team-member').forEach(m => m.classList.remove('active'));
    clickedMember.classList.add('active');
    teamGrid.classList.add('blurred');

    // Scroll to the details section
    detailsDiv.scrollIntoView({ behavior: 'smooth' });
}

// Close the details when clicking outside the grid
document.addEventListener('click', (event) => {
    if (!event.target.closest('.team-member')) {
        document.querySelectorAll('.team-member').forEach(m => m.classList.remove('active'));
        const currentDetails = document.querySelector('.dynamic-details');
        if (currentDetails) currentDetails.remove();
        teamGrid.classList.remove('blurred');
    }
});

renderTeamMembers();