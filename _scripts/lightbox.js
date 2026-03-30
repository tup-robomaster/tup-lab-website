(function() {
  const lightbox = {
    init() {
      this.createGallery();
      this.bindEvents();
    },

    createGallery() {
      // Create lightbox elements if they don't exist
      if (document.getElementById('lightbox-modal')) return;

      const modal = document.createElement('div');
      modal.id = 'lightbox-modal';
      modal.innerHTML = `
        <div class="lightbox-overlay"></div>
        <div class="lightbox-close">&times;</div>
        <div class="lightbox-prev">&#10094;</div>
        <div class="lightbox-next">&#10095;</div>
        <div class="lightbox-content">
          <img id="lightbox-img" src="" alt="">
          <div id="lightbox-caption"></div>
        </div>
      `;
      document.body.appendChild(modal);

      this.modal = modal;
      this.img = modal.querySelector('#lightbox-img');
      this.caption = modal.querySelector('#lightbox-caption');
      this.prevBtn = modal.querySelector('.lightbox-prev');
      this.nextBtn = modal.querySelector('.lightbox-next');
      
      this.currentIndex = 0;
      this.images = [];
    },

    bindEvents() {
      document.addEventListener('click', (e) => {
        const photoItem = e.target.closest('.photo-item:not(.more-tile)');
        if (photoItem) {
          e.preventDefault();
          this.openLightbox(photoItem);
        }

        if (e.target.classList.contains('lightbox-overlay') || e.target.classList.contains('lightbox-close')) {
          this.closeLightbox();
        }

        if (e.target.classList.contains('lightbox-prev')) {
          this.showPrev();
        }

        if (e.target.classList.contains('lightbox-next')) {
          this.showNext();
        }
      });

      document.addEventListener('keydown', (e) => {
        if (!this.modal.classList.contains('active')) return;
        if (e.key === 'Escape') this.closeLightbox();
        if (e.key === 'ArrowLeft') this.showPrev();
        if (e.key === 'ArrowRight') this.showNext();
      });
    },

    openLightbox(clickedItem) {
      // Refresh image list every time we open (in case of dynamic changes, though unlikely here)
      // Filter out 'more-tile'
      const grid = clickedItem.closest('.photo-grid');
      this.images = Array.from(grid.querySelectorAll('.photo-item:not(.more-tile) img')).map(img => ({
        src: img.src,
        alt: img.getAttribute('alt') || ''
      }));
      
      const clickedImg = clickedItem.querySelector('img');
      this.currentIndex = this.images.findIndex(img => img.src === clickedImg.src);
      
      this.updateDisplay();
      this.modal.classList.add('active');
      document.body.style.overflow = 'hidden';
    },

    closeLightbox() {
      this.modal.classList.remove('active');
      document.body.style.overflow = '';
    },

    updateDisplay() {
      const current = this.images[this.currentIndex];
      if (!current) return;
      
      this.img.src = current.src;
      this.caption.textContent = current.alt;
      
      // Toggle nav buttons
      this.prevBtn.style.display = this.images.length > 1 ? 'block' : 'none';
      this.nextBtn.style.display = this.images.length > 1 ? 'block' : 'none';
    },

    showPrev() {
      this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
      this.updateDisplay();
    },

    showNext() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
      this.updateDisplay();
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => lightbox.init());
  } else {
    lightbox.init();
  }
})();
