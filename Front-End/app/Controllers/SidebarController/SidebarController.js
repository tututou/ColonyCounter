angular
    .module('App.SidebarController', [])
    .controller('SidebarController', SidebarController);

SidebarController.$inject = [
    '$mdSidenav'
];
/**
 * Controller used to handle the operation of the sidebar.
 */
function SidebarController( $mdSidenav ) {

    var vm = this;
    // Sidebar items
    var imageSection = {
        name: 'Image Processing',
        rows: [
            {
                name: 'Process Images',
                iconClass: 'fa-picture-o',
                sref: 'site.home'
            },
            {
                name: 'View Results',
                iconClass: 'fa-list',
                sref: 'site.result'
            }
        ]
    }

    vm.close = close;
    vm.closeSideNavPanel = closeSideNavPanel;
    vm.menuSections = [
        imageSection
    ];

    init();

    function init() {

    }

    function closeSideNavPanel() {
        $mdSidenav('left').close();
    };
}