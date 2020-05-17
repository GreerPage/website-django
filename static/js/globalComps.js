class Loading extends React.Component {
    constructor() {
        super();
        this.messages = ['petting octocat...', 'flying to mars...', 'saving the tutrles...', 'catching gerbals...', 'feeding pidgeons...', 'waiting for backend wizards to awaken...', 'donating eyes to cyclopses...', 'hopping on one leg...', 'bootlegging nuclear launch codes...', 'crunching numbers...'];
        this.state = {message: this.messages[Math.floor(Math.random() * this.messages.length)]};
    }
    componentDidMount() {
        this.i = setInterval(() => {
            this.setState({message: this.messages[Math.floor(Math.random() * this.messages.length)]});
        }, 800);
    }
    componentWillUnmount() {
        clearInterval(this.i);
    }
    render() {
        return (
            r('div', {className: 'loading-box'},
                r('img', {src: '/static/images/loading-github.png'}),
                r('div', {className: 'loading-box-text'},
                    r('p', null, this.state.message)
                )
            )
        );
    }
}