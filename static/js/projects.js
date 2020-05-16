const r = React.createElement;

function GitContainer(props) {
    var name = props.name;
    var repo = props.data;
    return (
        r('div', {className: "repo-container", id: name}, 
            r('a', {className: 'git-link', href: repo.url, target: '_blank'}, name),
            r('div', {className: "lang-button", style: {backgroundColor: `${repo.languageColor}`}, onClick: () => DisplayIdToggle(name+'-hidden')}),
            r('div', {id: name+'-hidden', style: {display: 'none'}},
                r('span', {className: 'git-dot', style: {backgroundColor: `${repo.languageColor}`}}),
                r('span', null, repo.language)
            ),
            r('p', {style: {marginTop: '10px'}}, repo.description),
            r('a', {className: 'git-link', href: '/projects/' + name}, 'see more')
        )
    );
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
                 var info = Object.keys(data).map((val) => {
                    return r(GitContainer, {name: val, data: data[val], key: val});
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
