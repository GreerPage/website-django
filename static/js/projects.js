const r = React.createElement;

class Loading extends React.Component {
    constructor() {
        super();
        this.state = {dots: '.'};
    }
    text() {
        if (this.state.dots.length === 3) this.setState({dots: '.'});
        else if (this.state.dots.length === 2) this.setState({dots: '...'});
        else if (this.state.dots.length === 1) this.setState({dots: '..'});
    }
    componentDidMount() {
        this.i = setInterval(() => this.text(), 500);
    }
    componentWillUnmount() {
        clearInterval(this.i);
    }
    render() {
        return (
            r('div', {className: 'loading'}, r('p', null, this.state.dots))
        );
    }
}
class Git extends React.Component {
    constructor() {
        super();
        this.state = {loading: true};
    }
    render() {
        if (this.state.loading) {
            return r(Loading, null);
        }
    }
}

$(document).ready(() => {
    ReactDOM.render(
        r(Git, null, null),
        document.getElementById('root')
    ); 
})
