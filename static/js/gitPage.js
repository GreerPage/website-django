const r = React.createElement;


function highlight(str, lang) {
    if (lang && hljs.getLanguage(lang)) {
        try {
          return hljs.highlight(lang, str).value;
        } catch (__) {}
      }
  
      try {
        return hljs.highlightAuto(str).value;
      } catch (__) {}
  
      return '';
}

function LanguageBars(props) {
    var data = props.data;
    return (
        r('div', {className: 'language-bars-container', style: {borderRadius: '5px'}, onClick: () => displayList()}, 
            Object.keys(data).map((val, index) => {
                let info = data[val];
                return r(LanguageBar, {data: info, order: index, total: Object.keys(data).length, key: index});
            })
        )
    );
}

function LanguageBar(props) {
    var order = props.order;
    var data = props.data;
    var total = props.total;
    var style = {width: data.percent+'%', backgroundColor: data.color};
    if (order === 0) {
        style.borderBottomLeftRadius = '5px';
        style.borderTopLeftRadius = '5px';
    }
    if (order === total-1) {
        style.borderBottomRightRadius = '5px';
        style.borderTopRightRadius = '5px';
    }
    return r('span', {className: 'language-bars', style: style});
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
    var md = new Remarkable('full', {highlight: (str, lang) => highlight(str, lang)});
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
                r('div', {className: 'readmetop'}, r('p', {style: {margin: 0, paddingTop: '10px', paddingLeft: '10px'}}, 'README')),
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
                    r(LanguageBars, {data: this.state.data.languages}),
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