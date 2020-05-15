const r = React.createElement;

function LanguageBar(props) {
    var data = props.data;
    return (
        r('div', {className: 'language-bars-container', style: {borderRadius: '5px'}, onClick: () => displayList()}, 
            Object.keys(data).map((val, index) => {
                let info = data[val];
                if (index === 0) {
                    return r('span', {className: 'language-bars', style: {width: info.percent + '%', backgroundColor: info.color, borderBottomLeftRadius: '5px', borderTopLeftRadius: '5px'}, key: index});
                }
                else if (index === Object.keys(data).length-1) {
                    return r('span', {className: 'language-bars', style: {width: info.percent + '%', backgroundColor: info.color, borderBottomRightRadius: '5px', borderTopRightRadius: '5px'}, key: index}); 
                }
                return r('span', {className: 'language-bars', style: {width: info.percent + '%', backgroundColor: info.color}, key: index});
            })
        )
    );
}
function LanguageList(props) {
    var data = props.data;
    return (
        r('div', {className: 'git-langs-list-container', id: 'git-langs-list-container'},
            r('ul', {className: 'git-langs-list'},
                Object.keys(data).map((val, index) => {
                    let info = data[val];
                    return (
                        r('li', {key: index}, 
                            r('span', {className: 'git-dot', style : {backgroundColor: info.color}}),
                            r('span', null, val+ ' ', r('span', {id: 'Percent'}, `${info.percent}%`))
                        )
                    )
                })
            )
        )
    );
}
class GitPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {loading: true, data: ''};
    }
    getGitInfo() {
        fetch('/api/projects/' + this.props.name)
            .then(res => res.json())
            .then(data => {
                this.setState({data: data[this.props.name]});
                document.getElementById('gitpagelink').href = data[this.props.name].url
                this.setState({loading: false});
            });
    }
    componentDidMount() {
        this.getGitInfo();
    }
    render() {
        if (this.state.loading) {
            return r('div', null);
        }
        else {
            return (
                r('div', null, 
                    r(LanguageBar, {data: this.state.data.languages}),
                    r(LanguageList, {data: this.state.data.languages})
                )
            );
        }
    }
}

$(document).ready(() => {
    
    var reponame = window.location.pathname.replace('/projects/', '')
    ReactDOM.render(
        r(GitPage, {name: reponame}),
        document.getElementById('react-root')
    ); 
});