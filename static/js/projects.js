const r = React.createElement;

function Loading() {
    return r('img', {className: 'loading-image', src: '/static/images/loading.png'});
}
class Git extends React.Component {
    constructor() {
        super();
        this.state = {loading: true, data: ''};
    }
    getGitInfo() {
        fetch('api/projects')
            .then(res => res.json())
            .then(data => {
                 var info = Object.keys(data).map((val, key) => {
                    let repo = data[val];
                    return (
                        r('div', {className: "repo-container", id: val, key: key}, 
                            r('a', {className: 'git-link', href: repo.url, target: '_blank'}, val),
                            r('div', {className: "lang-button", style: {backgroundColor: `${repo.languageColor}`}, onClick: () => DisplayIdToggle(val+'-hidden')}),
                            r('div', {id: val+'-hidden', style: {display: 'none'}},
                                r('span', {className: 'git-dot', style: {backgroundColor: `${repo.languageColor}`}}),
                                r('span', null, repo.language)
                            ),
                            r('p', {style: {marginTop: '10px'}}, repo.description),
                            r('a', {className: 'git-link', href: '/projects/' + val}, 'see more')
                        )
                    );
                });
                this.setState({data: info});
                this.setState({loading: false});
            });
    }
    componentDidMount() {
        this.getGitInfo();
    }
    render() {
        if (this.state.loading) {
            return r(Loading, null);
        }
        else {
            return r('div', {className: 'repos-container'}, this.state.data);
        }
    }
}

$(document).ready(() => {
    ReactDOM.render(
        r(Git, null, null),
        document.getElementById('root')
    ); 
});
