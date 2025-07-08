
document.addEventListener('DOMContentLoaded', function () {
    if (typeof bookedDates !== 'undefined') {
        const formatDate = (dateStr) => new Date(dateStr).toISOString().split('T')[0];
        const booked = bookedDates.map(formatDate);

        ['id_check_in', 'id_check_out'].forEach((id) => {
            const input = document.getElementById(id);
            if (input) {
                input.addEventListener('input', function () {
                    const selected = this.value;
                    if (booked.includes(selected)) {
                        this.classList.add('is-invalid');
                    } else {
                        this.classList.remove('is-invalid');
                    }
                });
            }
        });
    }
});
