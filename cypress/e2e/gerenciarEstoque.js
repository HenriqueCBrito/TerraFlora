describe('Gerenciar Estoque de Insumos e Produtos', () => {
   
    after(() => {
        cy.exec('python ./create_superuser.py');
        cy.visit('/'); 
        cy.contains('Cadastro').click(); 
        cy.get('input[name="email"]').type('teste@teste.com');
        cy.get('input[name="username"]').type('usuarioTeste');
        cy.get('input[name="full_Name"]').type('Jorginho Silva');
        cy.get('input[name="cpf"]').type('12345678901');
        cy.get('input[name="phone_number"]').type('+5581912345678');
        cy.get('input[name="street"]').type('Cais do Apolo');
        cy.get('input[name="home_number"]').type('123');
        cy.get('input[name="city"]').type('Recife');
        cy.get('input[name="state"]').type('PE');
        cy.get('input[name="country"]').type('Brasil');
        cy.get('input[name="password"]').type('senha123');
        cy.get('input[name="confirm_password"]').type('senha123');
        cy.get('button[type="submit"]').click();
    });
    it('Adicionando produtos', () => {
        cy.contains('ARMAZENAMENTO').click();
    })
    after(() => {
        cy.visit('/admin/');
        cy.get('#id_username').type('admin@admin.com');  
        cy.get('#id_password').type('admin123'); 
        cy.get('.submit-row > input').click();
        cy.contains('Site administration').should('be.visible');
        cy.contains('Users').click();
        cy.get('#searchbar').type('teste@teste.com');
        cy.get('#changelist-search > div > [type="submit"]').click();
        cy.get('.action-select').click();  
        cy.get('select').select('Delete selected users');
        cy.get('.button').click();
        cy.get('div > [type="submit"]').click();
    });
    
    
});
