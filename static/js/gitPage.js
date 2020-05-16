const r = React.createElement;

class Loading extends React.Component {
    constructor() {
        super();
        this.messages = ['petting octocat...', 'fetching json...', 'waiting for github...', 'catching gerbals...', 'feeding pidgeons...', 'waiting for backend wizards to awaken...', 'donating eyes to cyclopses...'];
        this.state = {message: this.messages[Math.floor(Math.random() * this.messages.length)]};
    }
    componentDidMount() {
        this.i = setInterval(() => {
            this.setState({message: this.messages[Math.floor(Math.random() * this.messages.length)]})
        }, 800);
    }
    componentWillUnmount() {
        clearInterval(this.i)
    }
    render() {
        return (
            r('div', {className: 'loading-box'},
                r('img', {src: '/static/images/loading-github.png'}),
                r('div', {className: 'loading-box-text'},
                    r('p', null, this.state.message)
                )
            )
        )
    }
}

function LanguageBar(props) {
    var data = props.data;
    return (
        r('div', {className: 'language-bars-container', style: {borderRadius: '5px'}, onClick: () => displayList()}, 
            Object.keys(data).map((val, index) => {
                let info = data[val];
                if (Object.keys(data).length === 1) {
                    return r('span', {className: 'language-bars', style: {width: info.percent + '%', backgroundColor: info.color, borderRadius: '5px'}, key: index});
                }
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
function md(mark) {
    var md = new Remarkable();
    return {__html: md.render(mark)};
}
function ReadMe(props) {
    var readme = props.readme;
    if (readme === 'ERROR: Cannot find README.md in this repository :(') {
        return r('p', {style: {marginTop: '50px',}, dangerouslySetInnerHTML: md(readme)});
    }
    else {
        return (
            r('div', {className: 'readme'},
                r('div', {className: 'readmetop'}, r('p', {style: {margin: 0, paddingTop: '10px', paddingLeft: '10px'}}, 'README.md')),
                r('div', {style: { padding: '7%', paddingTop: '0px'}, dangerouslySetInnerHTML: md(readme)})
            )
        ) 
    }
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
            return r(Loading, null);
        }
        else {
            return (
                r('div', null, 
                    r(LanguageBar, {data: this.state.data.languages}),
                    r(LanguageList, {data: this.state.data.languages}),
                    r(ReadMe, {readme: this.state.data.readme})
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