(function () {
  // Inject the CSS once
  var style = document.createElement('style');
  style.textContent = [
    '.toc-collapsible {',
    '  overflow: hidden;',
    '  max-height: 0;',
    '  transition: max-height 0.28s cubic-bezier(0.4, 0, 0.2, 1),',
    '              opacity   0.22s ease;',
    '  opacity: 0;',
    '}',
    '.toc-collapsible.toc-open {',
    '  max-height: 1200px;',     /* big enough to fit any subtree */
    '  opacity: 1;',
    '}',
    '.toc-arrow {',
    '  cursor: pointer;',
    '  user-select: none;',
    '  display: inline-block;',
    '  font-size: 0.68em;',
    '  padding-left: 4px;',
    '  opacity: 0.40;',
    '  transition: transform 0.22s cubic-bezier(0.4, 0, 0.2, 1),',
    '              opacity   0.15s ease;',
    '  transform-origin: center center;',
    '}',
    '.toc-arrow.toc-arrow-open {',
    '  transform: rotate(90deg);',
    '  opacity: 0.75;',
    '}',
    '.toc-arrow:hover {',
    '  opacity: 1 !important;',
    '}',
  ].join('\n');
  document.head.appendChild(style);

  function initTocCollapse() {
    var tocMenu = document.querySelector('.toc__menu');
    if (!tocMenu) return;

    tocMenu.querySelectorAll('li').forEach(function (li) {
      // find direct child <ul>
      var childUl = null;
      for (var i = 0; i < li.children.length; i++) {
        if (li.children[i].tagName === 'UL') { childUl = li.children[i]; break; }
      }
      if (!childUl) return;

      var link = li.querySelector('a');
      if (!link) return;

      // mark the ul for animation
      childUl.classList.add('toc-collapsible');

      // add the arrow ▶
      var arrow = document.createElement('span');
      arrow.className = 'toc-arrow';
      arrow.textContent = '▶';
      link.appendChild(arrow);

      li.dataset.tocOpen = 'false';

      function toggle(e) {
        e.preventDefault();
        e.stopPropagation();
        var open = li.dataset.tocOpen === 'true';
        childUl.classList.toggle('toc-open', !open);
        arrow.classList.toggle('toc-arrow-open', !open);
        li.dataset.tocOpen = open ? 'false' : 'true';
      }

      arrow.addEventListener('click', toggle);
    });

    // Auto-expand the top-level items (h1-level) so the page
    // isn't totally empty on load — only the deep nesting is collapsed
    var topLevelOpen = tocMenu.querySelectorAll(':scope > li[data-toc-open]');
    topLevelOpen.forEach(function (li) {
      var arrow = li.querySelector('.toc-arrow');
      if (arrow) arrow.click();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTocCollapse);
  } else {
    initTocCollapse();
  }
})();
