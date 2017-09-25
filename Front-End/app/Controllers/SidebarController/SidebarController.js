angular
    .module('App.SidebarController', [])
    .controller('SidebarController', SidebarController);

SidebarController.$inject = [
    '$mdSidenav'
];

function SidebarController( $mdSidenav ) {

    var vm = this;
    var imageSection = {
        name: 'Image Processing',
        rows: [
            {
                name: 'Process Images',
                iconClass: 'fa-picture-o',
                sref: 'site.home'
            },
            {
                name: 'Image History',
                iconClass: 'fa-list',
                sref: 'site.history' // doesn't exist yet
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