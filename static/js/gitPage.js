const r = React.createElement;

function LanguageBar(props) {
    var data = props.data;
    return (
        r('div', {className: 'language-bars-container', style: {borderRadius: '5px'}}, 
            Object.keys(data).map((val, index) => {
                let info = data[val];
                if (index === 0) {
                    return r('span', {className: 'language-bars', style: {width: info.percent + '%', backgroundColor: info.color, borderBottomLeftRadius: '5px', borderTopLeftRadius: '5px'}, key: index})
                }
                else if (index === Object.keys(data).length-1) {
                    return r('span', {className: 'language-bars', style: {width: info.percent + '%', backgroundColor: info.color, borderBottomRightRadius: '5px', borderTopRightRadius: '5px'}, key: index}) 
                }
                return r('span', {className: 'language-bars', style: {width: info.percent + '%', backgroundColor: info.color}, key: index})
            })
        )
    );
}
function LanguageList (props) {
    var data = props.data;
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
                    r('a', {className: 'gitpagelink', href: this.state.data.url}, this.props.name),
                    r(LanguageBar, {data: this.state.data.languages})
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