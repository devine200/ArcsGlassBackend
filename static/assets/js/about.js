const teamGrid = document.getElementById('team-grid');

// Team members
const teamMembersData = [
    { id: 1, name: "OLAMIDE CLAUD-ENNIN", role: "Founder", image: "http://arcsglass.com/wp-content/uploads/2022/09/Olamide-scaled-e1706229664206-1699x2048.jpg", details: "Olamide is a lawyer by training. In 2018, herself and her partner, Imran Claud-Ennin developed and built their first project, A1/18. The project sold before completion and was one of most expensive properties developed in the estate at the time. She knew she had a passion for design and environmental development, so she completed a masters degree in social innovation and entrepreneurship at the London School of Economics.  Since 2019, she has spent her time designing and leading a team of incredibly intelligent people to deliver on impressive projects." },
    { id: 2, name: "IMRAN CLAUD-ENNIN", role: "Founder", image: "http://arcsglass.com/wp-content/uploads/2022/09/Imran-6-scaled-e1706229799196-1628x2048.jpg", details: "Imran is a creative director and project manager. He is a graduate of business and management from the university of Sussex. He has worked in the Real Estate sector for over 5 years, bringing the teams together and delivering on projects ranging from  construction of  apartment blocks to remodels and renovation." },
    { id: 3, name: "OLAMIDE CLAUD-ENNIN", role: "Founder", image: "http://arcsglass.com/wp-content/uploads/2022/09/Olamide-scaled-e1706229664206-1699x2048.jpg", details: "Olamide is a lawyer by training. In 2018, herself and her partner, Imran Claud-Ennin developed and built their first project, A1/18. The project sold before completion and was one of most expensive properties developed in the estate at the time. She knew she had a passion for design and environmental development, so she completed a masters degree in social innovation and entrepreneurship at the London School of Economics.  Since 2019, she has spent her time designing and leading a team of incredibly intelligent people to deliver on impressive projects." },
    { id: 4, name: "OLAMIDE CLAUD-ENNIN", role: "Founder", image: "http://arcsglass.com/wp-content/uploads/2022/09/Olamide-scaled-e1706229664206-1699x2048.jpg", details: "Olamide is a lawyer by training. In 2018, herself and her partner, Imran Claud-Ennin developed and built their first project, A1/18. The project sold before completion and was one of most expensive properties developed in the estate at the time. She knew she had a passion for design and environmental development, so she completed a masters degree in social innovation and entrepreneurship at the London School of Economics.  Since 2019, she has spent her time designing and leading a team of incredibly intelligent people to deliver on impressive projects." },
    { id: 5, name: "OLAMIDE CLAUD-ENNIN", role: "Founder", image: "http://arcsglass.com/wp-content/uploads/2022/09/Olamide-scaled-e1706229664206-1699x2048.jpg", details: "Olamide is a lawyer by training. In 2018, herself and her partner, Imran Claud-Ennin developed and built their first project, A1/18. The project sold before completion and was one of most expensive properties developed in the estate at the time. She knew she had a passion for design and environmental development, so she completed a masters degree in social innovation and entrepreneurship at the London School of Economics.  Since 2019, she has spent her time designing and leading a team of incredibly intelligent people to deliver on impressive projects." },
    { id: 6, name: "OLAMIDE CLAUD-ENNIN", role: "Founder", image: "http://arcsglass.com/wp-content/uploads/2022/09/Olamide-scaled-e1706229664206-1699x2048.jpg", details: "Olamide is a lawyer by training. In 2018, herself and her partner, Imran Claud-Ennin developed and built their first project, A1/18. The project sold before completion and was one of most expensive properties developed in the estate at the time. She knew she had a passion for design and environmental development, so she completed a masters degree in social innovation and entrepreneurship at the London School of Economics.  Since 2019, she has spent her time designing and leading a team of incredibly intelligent people to deliver on impressive projects." },
    // { id: 3, name: "Member 3", role: "Manager", image: "/images/man1.jpg", details: "Details about Member 3: Donec rutrum congue leo eget malesuada." },
    // { id: 4, name: "Member 4", role: "Marketer", image: "/images/man1.jpg", details: "Details about Member 4: Vivamus suscipit tortor eget felis porttitor volutpat." },
    // { id: 5, name: "Member 5", role: "HR", image: "/images/man1.jpg", details: "Details about Member 5: Nulla porttitor accumsan tincidunt." },
    // { id: 6, name: "Member 6", role: "Support", image: "/images/man1.jpg", details: "Details about Member 6: Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a." },
    // { id: 7, name: "Member 7", role: "Developer", image: "/images/man1.jpg", details: "Details about Member 7: Quisque velit nisi, pretium ut lacinia in, elementum id enim." },
    // { id: 8, name: "Member 8", role: "Designer", image: "/images/man1.jpg", details: "Details about Member 8: Nulla quis lorem ut libero malesuada feugiat." },
    // { id: 9, name: "Member 9", role: "Manager", image: "/images/man1.jpg", details: "Details about Member 9: Pellentesque in ipsum id orci porta dapibus." },
    // { id: 10, name: "Member 10", role: "Marketer", image: "/images/man1.jpg", details: "Details about Member 10: Vestibulum ante ipsum primis in faucibus orci luctus." },
    // { id: 11, name: "Member 11", role: "HR", image: "/images/man1.jpg", details: "Details about Member 11: Proin eget tortor risus." },
    // {
    //     id: 12, name: "Member 12", role: "Support", image: "/images/man1.jpg", details: `Details about Member 12: Curabitur arcu erat, accumsan id imperdiet et, porttitor 
    //     Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur laboriosam dolorum dicta, corporis assumenda error beatae fugiat! Iste, aliquid, eius eligendi inventore nobis tempora similique ex sit ea, accusantium omnis.
    //     at sem.` },
];

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