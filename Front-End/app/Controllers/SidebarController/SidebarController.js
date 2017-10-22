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
    // Image related sidebar items
    var imageSection = {
        name: 'Image Processing',
        rows: [
            {
                name: 'Process Images',
                iconClass: 'fa-picture-o',
                sref: 'site.home',
                href: '#'
            },
            {
                name: 'View Results',
                iconClass: 'fa-list',
                sref: 'site.result',
                href: '#'
            }
        ]
    };

    var feedbackSection = {
        name: 'Beta Release',
        rows: [
            {
                name: 'Report Bugs',
                iconClass: 'fa-bug',
                sref: undefined,
                href: 'https://github.com/abarganier/ColonyCounter/issues'
            },
            {
                name: 'Testing Feedback',
                iconClass: 'fa-question',
                sref: undefined,
                href: 'https://drive.google.com/open?id=1IyBDMSYjehq9KFSHP_k-6gV8pzyk5k3dN1Nhn-Wfloc'
            }
        ]
    }
    vm.close = close;
    vm.closeSideNavPanel = closeSideNavPanel;
    vm.menuSections = [
        imageSection,
        feedbackSection
    ];

    init();

    function init() {

    }

    function closeSideNavPanel() {
        $mdSidenav('left').close();
    };
}